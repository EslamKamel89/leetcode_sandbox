<?php

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {
    private function reverse($head) {
        $current = $head;
        $previous = null;
        while ($current) {
            $nextNode = $current->next;
            $current->next = $previous;
            $previous = $current;
            $current = $nextNode;
        }
        return $previous;
    }

    /**
     * @param ListNode $head
     * @return Boolean
     */
    function isPalindrome($head) {
        $slow = $head;
        $fast = $head;
        while ($fast && $fast->next) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }
        $left = $head;
        $right = $this->reverse($slow);
        while ($left and $right) {
            if ($left->val != $right->val) {
                return false;
            }
            $left = $left->next;
            $right = $right->next;
        }
        return true;
    }
}
