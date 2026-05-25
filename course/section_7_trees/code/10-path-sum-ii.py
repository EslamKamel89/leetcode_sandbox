from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def dfs(root: Optional[TreeNode], nodes: list[int]) -> list[int]:
            # print('------------------------')
            # print(root.val if root else None)
            # print(nodes)
            if not root:
                return nodes
            nodes = [*nodes, root.val]
            if not root.left and not root.right and sum(nodes) == targetSum:
                self.res.append(nodes)
                return nodes
            dfs(root.left, nodes)
            dfs(root.right, nodes)
            return nodes

        dfs(root, [])
        return self.res
