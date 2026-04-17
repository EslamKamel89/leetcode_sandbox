from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[right] + nums[left]
                if total < target:
                    result += right - left
                    left += 1
                else:
                    right -= 1
        return result
