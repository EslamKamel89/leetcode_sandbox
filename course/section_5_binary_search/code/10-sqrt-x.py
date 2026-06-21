class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            m = (left + right) // 2
            sqr = m**2
            if sqr == x:
                return m
            if sqr > x:
                right = m - 1
            else:
                left = m + 1
        return left - 1
