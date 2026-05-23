from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        stack = [root]
        while stack:
            for i in range(len(stack)):
                if not stack:
                    break
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            level += 1
        return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 1
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                if node.left:
                    stack.append([node.left, depth + 1])
                    res = max(res, depth + 1)
                if node.right:
                    stack.append([node.right, depth + 1])
                    res = max(res, depth + 1)
        return res
