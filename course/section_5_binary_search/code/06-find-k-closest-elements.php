<?php

class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @param Integer $x
     * @return Integer[]
     */
    function findClosestElements($arr, $k, $x) {
        $left = 0 ;
        $right = count($arr) - 1 ;
        while(($right - $left) >= $k ){
            if(abs($arr[$left] - $x) > abs($arr[$right] - $x)){
                $left++ ;
            } else {
                $right-- ;
            }
        }
        return array_slice($arr , $left , $right - $left +1) ;
    }
}