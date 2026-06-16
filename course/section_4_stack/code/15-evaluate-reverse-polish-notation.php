<?php

class Solution {

    /**
     * @param String[] $tokens
     * @return Integer
     */
    function evalRPN($tokens) {
        $stack = [];
        foreach ($tokens as $token) {
            if ($token === '+') {
                $stack[] = array_pop($stack) + array_pop($stack);
            } elseif ($token === '*') {
                $stack[] = array_pop($stack) * array_pop($stack);
            } elseif ($token === '/') {
                $num2 = array_pop($stack);
                $num1 = array_pop($stack);
                $stack[] = (int)($num1 / $num2);
            } elseif ($token === '-') {
                $num2 = array_pop($stack);
                $num1 = array_pop($stack);
                $stack[] =  $num1 - $num2;
            } else {
                $stack[] = (int)$token;
            }
        }
        return $stack[0];
    }
}
