<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function search($nums, $target) {
        $left = 0  ;
        $right = count($nums) - 1 ;
        while($left <= $right){
            $m = intdiv($left + $right , 2) ;
            $mid = $nums[$m] ;
            if($mid == $target){
                return $m ;
            }
            if($mid >= $nums[0]){
                // left portion 
                if($mid < $target || $target < $nums[0]){
                    $left = $m + 1 ;
                } else {
                    $right = $m - 1 ;
                }
            } else {
                // right portion
                if($mid > $target || $target > $nums[count($nums) - 1]){
                    $right = $m - 1 ;
                } else {
                    $left = $m + 1 ;
                }
            }
        }
        return -1;
    }
}