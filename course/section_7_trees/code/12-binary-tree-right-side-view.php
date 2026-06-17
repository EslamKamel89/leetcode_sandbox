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

    /**
     * @param TreeNode $root
     * @return Integer[]
     */
    function rightSideView($root) {
        $queue = new SplQueue();
        $queue->enqueue($root);
        $res = [];
        while (!$queue->isEmpty()) {
            $size = $queue->count();
            $level = [];
            for ($i = 0; $i < $size; $i++) {
                $node = $queue->dequeue();
                if ($node !== null) {
                    $level[] = $node->val;
                    $queue->enqueue($node->left);
                    $queue->enqueue($node->right);
                }
            }
            if (!empty($level)) {
                $res[] = $level[count($level) - 1];
            }
        }
        return $res;
    }
}
