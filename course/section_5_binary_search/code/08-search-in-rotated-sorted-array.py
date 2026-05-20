from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            mid = nums[m]
            if target == mid:
                return m
            if mid >= nums[l]:
                # left protion
                if mid <= target or target < nums[l]:
                    # have to sarch to the right
                    l = m + 1
                else:
                    r = m - 1
            else:
                # we are in the right portion
                if mid >= target or target > nums[r]:
                    # have to search the left
                    r = m - 1
                else:
                    # have to search the right
                    l = m + 1
        return -1
