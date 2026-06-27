<?php


 class TreeNode {
     public $val = null;
     public $left = null;
     public $right = null;
     function __construct($val = 0, $left = null, $right = null) {
         $this->val = $val;
         $this->left = $left;
         $this->right = $right;
     }
 }
 
class Solution {
    private array $seen = [] ;
    private function inOrder($node){
        if($node===null) return ;
        $this->inOrder($node->left);
        $this->seen[] = $node->val;
        $this->inOrder($node->right);
    }

    /**
     * @param TreeNode $root
     * @param Integer $k
     * @return Boolean
     */
    function findTarget($root, $k) {
        $this->inOrder($root);
        $left = 0 ;
        $right = count($this->seen) - 1 ;
        while($left < $right){
            $total = $this->seen[$left] + $this->seen[$right] ; 
            if($total === $k) return true ;
            elseif($total > $k) $right-- ;
            else $left++ ;
        }
        return false ;
    }
}