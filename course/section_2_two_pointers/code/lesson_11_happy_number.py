class Solution:
    def next(self, n: int) -> int:
        nums: list[int] = [int(num) for num in str(n)]
        result = 0
        for num in nums:
            result += num**2
        return result

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        slow = n
        fast = n
        while True:
            slow = self.next(slow)
            fast = self.next(self.next(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
