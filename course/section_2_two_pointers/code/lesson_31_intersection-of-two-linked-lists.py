# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def pr[T](val: T, title: str = "") -> T:
    print(title, val)
    return val


class Solution:
    def getIntersectionNode1(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        seen = set()
        while headA or headB:
            # print('-------------------------')
            # print('a = ' , headA.val if headA else None)
            # print('b = ' , headB.val if headB else None)
            if headA == headB:
                return headA
            if headA in seen:
                return headA
            if headB in seen:
                return headB
            if headA:
                seen.add(headA)
                headA = headA.next
            if headB:
                seen.add(headB)
                headB = headB.next
        return None

    def getIntersectionNode2(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pA = headA
        pB = headB
        lenA = 0
        lenB = 0
        while pA and pA.next:
            lenA += 1
            pA = pA.next
        while headB and pB.next:
            lenB += 1
            pB = pB.next
        if pA != pB:
            return None
        else:
            lenA += 1
            lenB += 1
            # print('lenA = ' , lenA)
            # print('lenB = ' , lenB)
            pA = headA
            pB = headB
            if lenA > lenB:
                for i in range(lenA - lenB):
                    pA = pA.next
            elif lenA < lenB:
                for i in range(lenB - lenA):
                    pB = pB.next
            while pA and pB:
                if pA == pB:
                    return pA
                pA = pA.next
                pB = pB.next

    def getIntersectionNode3(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA.next or pB.next:
            pA = pA.next if pA.next else pA
            pB = pB.next if pB.next else pB
        if pA != pB:
            return
        pA = headA
        pB = headB
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next if pA.next else headB
            pB = pB.next if pB.next else headA

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
