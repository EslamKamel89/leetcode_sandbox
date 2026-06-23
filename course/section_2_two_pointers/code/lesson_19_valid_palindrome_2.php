<?php


class Solution {
    private function isValidRange($s , $left , $right){
        while($left<=$right){
            if($s[$left]!=$s[$right]){
                return false ;
            }
            $left++;
            $right--;
        }
        return true ;
    }

    /**
     * @param String $s
     * @return Boolean
     */
    function validPalindrome($s) {
        $left = 0 ;
        $right = strlen($s) - 1 ; 
        while($left <= $right){
            if($s[$left] != $s[$right]){
                return $this->isValidRange($s , $left+1 , $right) || $this->isValidRange($s , $left , $right-1);
            }
            $left++;
            $right--;
        }
        return true ;
    }
}