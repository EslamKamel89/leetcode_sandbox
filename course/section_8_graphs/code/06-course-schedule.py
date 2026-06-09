from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(crs: int) -> bool:
            state = states[crs]
            if state == VISITED:
                return True
            if state == VISITING:
                return False
            states[crs] = VISITING
            for nei in adj[crs]:
                if not dfs(nei):
                    return False
            states[crs] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
