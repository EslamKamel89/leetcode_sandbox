<?php

class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minPathSum($grid) {
        for($r = 0 ; $r < count($grid); $r++){
            for($c = 0 ; $c < count($grid[0]); $c++){
                if($r === 0 && $c !== 0){
                    $grid[$r][$c] += $grid[$r][$c-1];
                } elseif($c === 0 && $r !== 0){
                    $grid[$r][$c] += $grid[$r-1][$c] ;
                } elseif($c !== 0 && $r !== 0) {
                    $grid[$r][$c] += min($grid[$r-1][$c] , $grid[$r][$c-1]) ; 
                } 
            }
        }
        return $grid[count($grid)-1][count($grid[0])-1] ;
        
    }
}