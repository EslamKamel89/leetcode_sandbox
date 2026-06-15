from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if r == 0 and c != 0:
                    grid[r][c] += grid[r][c - 1]
                elif c == 0 and r != 0:
                    grid[r][c] += grid[r - 1][c]
                elif r != 0 and c != 0:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        return grid[r][c] # type: ignore
