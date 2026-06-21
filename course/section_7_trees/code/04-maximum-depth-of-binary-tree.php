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
    function maxDepth($root) {
        if (!$root) {
            return 0;
        }
        return 1 + max($this->maxDepth($root->left), $this->maxDepth($root->right));
    }
}
