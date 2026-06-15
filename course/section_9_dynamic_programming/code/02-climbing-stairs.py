class Solution:
    def climbStairs1(self, n: int) -> int:
        if n <= 2:
            return n
        tab = [0] * (n + 1)
        tab[1] = 1
        tab[2] = 2
        for i in range(3, n + 1):
            tab[i] = tab[i - 1] + tab[i - 2]
        return tab[n]

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev2 = 1
        prev1 = 2
        for _ in range(3, n + 1):
            prev2, prev1 = prev1, prev1 + prev2
        return prev1
