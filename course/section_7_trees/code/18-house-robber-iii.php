<?php

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {
    private function dfs($node) {
        if ($node === null) {
            return [0, 0];
        }
        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);
        return [
            $node->val + $left[1] + $right[1],
            max($left) + max($right)
        ];
    }

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function rob($root) {
        return max($this->dfs($root));
    }
}
