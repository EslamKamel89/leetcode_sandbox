<?php

class Solution {

  
    function sortColors(&$nums) {
        $left = 0 ;
        for($i = 0 ; $i < count($nums); $i++){
            if($nums[$i] === 0){
                $temp = $nums[$i] ; 
                $nums[$i] = $nums[$left] ;
                $nums[$left] = $temp ; 
                $left++ ;
            }
        }
        for($j = $left; $j < count($nums); $j++){
            if($nums[$j] === 1 ){
                $temp = $nums[$j] ; 
                $nums[$j] = $nums[$left] ; 
                $nums[$left] = $temp ;
                $left++ ;
            }
        }
        
    }
}