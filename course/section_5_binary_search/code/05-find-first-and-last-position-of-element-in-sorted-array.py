from typing import List


class Solution:

    def binary_search(self, nums: list[int], target: int, left_biased: bool) -> int:
        l, r, i = 0, len(nums) - 1, -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                i = m
                if left_biased:
                    r = m - 1
                else:
                    l = m + 1
        return i

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.binary_search(nums, target, True),
            self.binary_search(nums, target, False),
        ]
