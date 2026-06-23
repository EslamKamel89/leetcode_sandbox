<?php
class Solution {

    /**
     * @param Integer[] $pushed
     * @param Integer[] $popped
     * @return Boolean
     */
    function validateStackSequences($pushed, $popped) {
        $stack = [] ;
        $i = 0 ; 
        foreach($pushed as $num){
            $stack[] = $num ; 
            while(!empty($stack) && $i < count($popped) && $stack[count($stack)-1] == $popped[$i]){
                array_pop($stack);
                $i++;
            }
        }
        return empty($stack);
        
    }
}