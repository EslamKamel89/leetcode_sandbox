from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if j <= i:
                    continue
                if (num1 + num2) == target:
                    return [i, j]
        return []


res = Solution().twoSum(nums=[3, 2, 4], target=6)
print(res)
