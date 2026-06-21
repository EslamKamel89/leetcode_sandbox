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

    def reverse(self, head):
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

    def isPalindrome(self, head):

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left = head
        right = self.reverse(slow)

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
