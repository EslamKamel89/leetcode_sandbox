class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0
        while left <= right:
            m = (left + right) // 2
            square = m**2
            if square > x:
                right = m - 1
            else:
                res = m
                left = m + 1
        return res
