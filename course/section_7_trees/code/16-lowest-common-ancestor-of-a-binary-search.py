# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor1(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":  # type: ignore
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.ans = None

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            if node.val == p.val or node.val == q.val:
                self.ans = node
                return
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
            elif p.val < node.val and q.val < node.val:
                dfs(node.left)
            else:
                self.ans = node
                return

        dfs(root)
        return self.ans  # type: ignore
