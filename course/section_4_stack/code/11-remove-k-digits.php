<?php

class Solution {
    function removeKdigits($num, $k) {
        $stack = [] ; 
        for($i = 0 ; $i < strlen($num); $i++) {
            $c = $num[$i] ; 
            while($k > 0 && !empty($stack) && end($stack) > $c){
                array_pop($stack);
                $k-- ;
            }
            $stack[] = $c ;
        }
        while($k > 0){
            array_pop($stack);
            $k--;
        }
        $res = ltrim(implode('', $stack) , '0');
        return $res === '' ? '0' : $res ;
    }
}