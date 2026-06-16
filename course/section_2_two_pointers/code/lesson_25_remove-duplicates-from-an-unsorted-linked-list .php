<?php

class ListNode {
    public $val = 0;
    public $next = null;
    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}
class Solution {

    /**
     * @param ListNode $head
     * @return ListNode
     */
    function deleteDuplicatesUnsorted($head) {
        $freq = [];
        $curr = $head;
        while ($curr != null) {
            if (!isset($freq[$curr->val])) {
                $freq[$curr->val] = 0;
            }
            $freq[$curr->val]++;
            $curr = $curr->next;
        }
        $curr = $head;
        $prev = new ListNode();
        $new_head =  $prev;
        while ($curr != null) {
            if ($freq[$curr->val] == 1) {
                $prev->next = $curr;
                $prev = $curr;
            }
            $curr = $curr->next;
        }
        $prev->next = null;
        return $new_head->next;
    }
}
