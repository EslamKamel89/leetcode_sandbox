from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res
