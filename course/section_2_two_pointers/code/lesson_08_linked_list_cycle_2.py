from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getMeetingPoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = self.getMeetingPoint(head)
        if pointer is None:
            return None
        current = head
        while current != pointer:
            pointer = pointer.next  # type: ignore
            current = current.next  # type: ignore
        return current
