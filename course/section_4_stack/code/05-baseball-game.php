<?php

class Solution {

    /**
     * @param String[] $operations
     * @return Integer
     */
    function calPoints($operations) {
        $stack = [];
        foreach ($operations as $token) {
            if ($token === 'C') {
                array_pop($stack);
            } elseif ($token === '+') {
                $stack[] = $stack[count($stack) - 1] + $stack[count($stack) - 2];
            } elseif ($token === 'D') {
                $stack[] = $stack[count($stack) - 1] * 2;
            } else {
                $stack[] = (int)$token;
            }
        }
        // var_dump($stack) ;
        return array_sum($stack);
    }
}
