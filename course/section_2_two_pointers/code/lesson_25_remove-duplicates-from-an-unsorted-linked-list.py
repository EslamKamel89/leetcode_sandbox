# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from collections import defaultdict


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq = defaultdict(int)
        current = head
        while current:
            freq[current.val] += 1
            current = current.next
        current = head
        previous = ListNode()
        new_head = previous
        while current:
            if freq[current.val] == 1:
                previous.next = current
                previous = current
            current = current.next
        previous.next = None
        return new_head.next  # type: ignore
