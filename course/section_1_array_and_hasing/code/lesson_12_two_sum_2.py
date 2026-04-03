from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = 1
        while slow < len(numbers):
            while fast < len(numbers):
                if (numbers[slow] + numbers[fast]) == target:
                    return [slow + 1, fast + 1]
                fast = fast + 1
            slow = slow + 1
        return []

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum > target:
                right -= 1
            if sum < target:
                left += 1
        return []
