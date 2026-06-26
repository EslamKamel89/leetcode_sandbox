<?php

class Solution {

    /**
     * @param Integer $target
     * @param Integer[] $nums
     * @return Integer
     */
    function minSubArrayLen($target, $nums) {
        $total = 0  ;
        $min_count = PHP_INT_MAX ;
        $start = 0 ;
        for($end = 0 ; $end < count($nums) ; $end++){
            $total += $nums[$end] ;
            while($total >= $target) {
                $min_count = min($min_count , $end - $start + 1) ;
                $total -= $nums[$start] ;
                $start++ ;
            }
        }
        return $min_count === PHP_INT_MAX ? 0 : $min_count ;
    }
}