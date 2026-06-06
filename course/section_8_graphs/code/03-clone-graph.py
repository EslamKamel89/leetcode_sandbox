class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node :
            return None 
        o_to_n = {}
        visited = set() 
        def dfs(node:Optional[Node]):
            if not node :
                return None 
            visited.add(node)
            o_to_n[node] = Node(node.val)
            for nei in node.neighbors :
                if nei not in visited :
                    dfs(nei)
        dfs(node)
        for old , new in o_to_n.items():
            for nei in old.neighbors :
                new.neighbors.append(o_to_n[nei])
        return o_to_n[node]
