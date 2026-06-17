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
    private bool $isBalanced = true;
    private function dfs(?TreeNode $node) {
        if ($node === null) {
            return 0;
        }
        $left = $this->dfs($node->left);
        $right = $this->dfs($node->right);
        if (abs($left - $right) > 1) {
            $this->isBalanced = false;
            return 0;
        }
        return 1 + max($left, $right);
    }

    /**
     * @param TreeNode $root
     * @return Boolean
     */
    function isBalanced($root) {
        $this->dfs($root);
        return $this->isBalanced;
    }
}
