from typing import List


def pr[T](val: T, title="") -> T:
    print(title, val)
    return val


class Solution:
    def findMin1(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            mid = nums[m]
            if mid >= nums[0]:
                left = m + 1
            else:
                right = m - 1
        if left < len(nums):
            return nums[left]
        else:
            return nums[0]

    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                break
            m = (left + right) // 2
            res = min(nums[m], res)
            if nums[left] <= nums[m]:
                left = m + 1
            else:
                right = m - 1
        return res
