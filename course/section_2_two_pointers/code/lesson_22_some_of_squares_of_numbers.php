<?php

class Solution {

    /**
     * @param Integer $c
     * @return Boolean
     */
    function judgeSquareSum($c) {
        $left = 0;
        $right = (int)(sqrt($c));
        while ($left <= $right) {
            $squareSum = $left ** 2 + $right ** 2;
            if ($squareSum == $c) {
                return true;
            }
            if ($squareSum > $c) {
                $right--;
            } else {
                $left++;
            }
        }
        return false;
    }
}
