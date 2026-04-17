# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pr[T](val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def findTarget1(self, root: Optional[TreeNode], k: int) -> bool:
        seen = []

        def inner(current: Optional[TreeNode]) -> bool:
            if not current:
                return False
            target = k - current.val
            if target in seen:
                return True
            seen.append(current.val)
            return inner(current.right) or inner(current.left)

        result = inner(root)
        print("seen = ", list(seen))
        return result

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            inorder(node.left)
            seen.append(node.val)
            inorder(node.right)

        inorder(root)
        left = 0
        right = len(seen) - 1
        while left < right:
            total = seen[left] + seen[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        return False
