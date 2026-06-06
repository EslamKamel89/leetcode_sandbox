from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        minutes = 0
        fresh_num = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh_num += 1
        if fresh_num == 0:
            return 0
        while queue:
            minutes += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for r, c in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == FRESH :
                        grid[r][c] = ROTTEN 
                        fresh_num -= 1 
                        queue.append((r,c))
        return minutes-1 if fresh_num == 0 else -1
