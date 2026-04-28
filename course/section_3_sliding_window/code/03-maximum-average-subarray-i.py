from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i]
            current_sum -= nums[i - k]
            max_sum = max(current_sum, max_sum)
        return max_sum / k
