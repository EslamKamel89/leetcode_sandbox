<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMin($nums) {
        $left = 0;
        $right = count($nums) - 1;
        while ($left <= $right) {
            $m = intdiv($left + $right, 2);
            $mid = $nums[$m];
            if ($mid >= $nums[0]) {
                $left = $m + 1;
            } else {
                $right = $m - 1;
            }
        }
        return $left < count($nums) ? $nums[$left] : $nums[0];
    }
}
