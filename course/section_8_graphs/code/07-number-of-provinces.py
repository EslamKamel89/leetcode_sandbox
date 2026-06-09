from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            if i in self.visited :
                return 
            self.visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)

        provinces = 0
        self.visited = set()
        n = len(isConnected)
        for i in range(n):
            if i not in self.visited:
                provinces += 1
                dfs(i)

        return provinces
