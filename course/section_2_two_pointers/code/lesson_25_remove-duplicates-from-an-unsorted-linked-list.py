# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pr[T](val, title: str = "") -> T:
    print(title, val)
    return val


class Solution:
    def deleteDuplicatesUnsorted1(self, head: ListNode) -> ListNode:
        seen: dict[int, list] = {}
        current = head
        while current:
            if current.val in seen:
                seen[current.val][1] += 1
            else:
                seen[current.val] = [current, 1]
            current = current.next
        current_head = None
        prev = None
        for node_info in seen.values():
            if node_info[1] != 1:
                continue
            if prev != None:
                prev.next = node_info[0]
            else:
                current_head = node_info[0]
            prev = node_info[0]
        if prev:
            prev.next = None
        return current_head

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        freq: dict[int, int] = {}
        current = head
        while current:
            freq[current.val] = freq.get(current.val, 0) + 1
            current = current.next
        # print(freq)
        current = head
        prev = ListNode()
        new_head = prev
        while current:
            if freq[current.val] == 1:
                prev.next = current
                prev = current
            current = current.next
        prev.next = None
        return new_head.next
