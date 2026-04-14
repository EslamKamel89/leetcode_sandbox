from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        vals = []
        current = head
        while current:
            vals.append(current.val)
            current = current.next
        return vals == vals[::-1]

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        # find the middle of the linked list (slow)
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
        # reverse the direction
        prev: Optional[ListNode] = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        assert prev is not None
        # check if this linked list is a palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:  # type: ignore
                return False
            left = left.next  # type: ignore
            right = right.next
        return True
