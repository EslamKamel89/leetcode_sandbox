from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return [0, 0]
            left_pair = dfs(root.left)
            right_pair = dfs(root.right)
            with_root = root.val + left_pair[1] + right_pair[1]
            without_root = max(left_pair) + max(right_pair)
            return [with_root, without_root]

        return max(dfs(root))
