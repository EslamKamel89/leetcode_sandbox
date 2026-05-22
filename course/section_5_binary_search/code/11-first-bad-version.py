# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            m = (left + right) // 2
            if isBadVersion(m):  # type: ignore
                right = m - 1
            else:
                left = m + 1
        return left
