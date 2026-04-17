# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pr[T](val, title: str = "") -> T:
    print(title, val)
    return val


class Solution:
    def partition1(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = []
        gte = []
        current = head
        while current:
            if current.val < x:
                lt.append(current)
            else:
                gte.append(current)
            current = current.next
        sorted_list = lt + gte
        # print([x.val for x in sorted_list])
        for i in range(len(sorted_list)):
            sorted_list[i].next = (
                sorted_list[i + 1] if i < len(sorted_list) - 1 else None
            )
        return sorted_list[0] if sorted_list else None

    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt = []
        gte = []
        current = head
        while current:
            if current.val < x:
                lt.append(current.val)
            else:
                gte.append(current.val)
            current = current.next
        current = head
        for val in lt + gte:
            current.val = val  # type: ignore
            current = current.next  # type: ignore
        return head

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lt_head: ListNode = ListNode()
        lt: Optional[ListNode] = lt_head
        gte_head: ListNode = ListNode()
        gte: Optional[ListNode] = gte_head
        while head:
            if head.val < x:
                lt.next = head
                lt = lt.next
            else:
                gte.next = head
                gte = gte.next
            head = head.next

        lt.next = gte_head.next
        gte.next = None
        return lt_head.next
