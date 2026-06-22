<?php

class Solution {
    private function dfs(int $i , int $j){
        if($i < 0 || $i >= $this->m || $j < 0 || $j >= $this->n || $this->grid[$i][$j] !== '1') return ;
        $this->grid[$i][$j] = '0' ;
        $this->dfs($i+1 , $j);
        $this->dfs($i-1 , $j);
        $this->dfs($i , $j+1);
        $this->dfs($i , $j-1);
    }

    /**
     * @param String[][] $grid
     * @return Integer
     */
    function numIslands($grid) {
        $this->grid = $grid  ;
        $this->m = count($grid);
        $this->n = count($grid[0]) ;
        $numOfIslands = 0 ;
        for($i = 0 ; $i < $this->m ; $i++){
            for($j = 0 ; $j < $this->n ; $j++){
                if($this->grid[$i][$j] === '1') {
                    $numOfIslands += 1 ; 
                    $this->dfs($i , $j) ;
                }
            }
        }
        return $numOfIslands ;
    }
}