# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True 
        def dfs(node:Optional[TreeNode]) :
            if not node :
                return 0 
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right) > 1 :
                self.balanced = False
                return 0 
            return 1 + max(left, right)
        dfs(root)
        return self.balanced
        