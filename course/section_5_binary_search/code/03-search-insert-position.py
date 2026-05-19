from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        l, r = 0, len(nums) - 1
        m = 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l
        # try:
        #     return m if nums[m] > target and nums[m + 1] < target else m + 1
        # except:
        #     return m
