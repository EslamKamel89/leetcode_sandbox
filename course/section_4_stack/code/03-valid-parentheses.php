<?php
class Solution {
    function isValid($s) {
        $stack = [];
        for($i = 0 ; $i < strlen($s); $i++){
            $bracket = $s[$i];
            if($bracket === '[' || $bracket === '(' || $bracket === '{'){
                $stack[] = $bracket ;
            } else {
                if(empty($stack)){
                    return false ;
                } elseif(end($stack) === '(' and $bracket === ')'){
                    array_pop($stack);
                } elseif(end($stack) === '[' and $bracket === ']') {
                    array_pop($stack);
                } elseif(end($stack) === '{' and $bracket === '}') {
                    array_pop($stack);
                } else {
                    return false ;
                }
            }
        }
        return empty($stack);
    }
}