class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            m = (left + right) // 2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        return nums[left]
