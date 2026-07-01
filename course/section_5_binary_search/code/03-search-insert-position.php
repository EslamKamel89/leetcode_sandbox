<?php

class Solution {

    function searchInsert($nums, $target) {
        $left = 0 ;
        $right = count($nums) - 1  ;
        while($left<=$right){
            $m = intdiv($left + $right , 2) ;
            $mid = $nums[$m] ;
            if($mid === $target){
                return $m ;
            } elseif($mid > $target){
                $right = $m - 1 ;
            } else {
                $left = $m + 1 ;
            }
        }
        return $left ;
    }
}