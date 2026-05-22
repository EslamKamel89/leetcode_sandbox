class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            m = (left + right) // 2
            sqr = m**2
            if sqr == num:
                return True
            if sqr > num:
                right = m - 1
            else:
                left = m + 1
        return False
