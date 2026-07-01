<?php

class Solution {
    function isPerfectSquare($num) {
        $left = 0 ;
        $right = $num ; 
        while($left <= $right){
            $m = intdiv($left + $right , 2) ;
            $square = $m * $m ;
            if($square=== $num){
                return True; 
            } elseif( $square > $num){
                $right = $m - 1; 
            } else {
                $left = $m + 1 ;
            }
        }
        return False ;
    }
}