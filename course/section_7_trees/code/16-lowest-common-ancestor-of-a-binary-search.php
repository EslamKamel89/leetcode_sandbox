<?php

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($value) { $this->val = $value; }
 * }
 */

class Solution {
    private $ans = null ;
    private function dfs( $node , $p , $q){
        if($node === null) return ; 
        if($node === $p or $node === $q ){
            $this->ans = $node ;
            return ;
        }
        if($p->val > $node->val && $q->val > $node->val){
            $this->dfs($node->right , $p , $q) ;
        } elseif ($p->val < $node->val && $q->val < $node->val){
            $this->dfs($node->left , $p , $q) ;
        } else {
            $this->ans = $node ;
            return ;
        }
    }
   
    function lowestCommonAncestor($root, $p, $q) {
        $this->dfs($root , $p , $q);
        return $this->ans ;
        
    }
}