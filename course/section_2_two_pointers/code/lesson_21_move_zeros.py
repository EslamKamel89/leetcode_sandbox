from typing import List


class Solution:
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[write] = nums[write], nums[i]
                write += 1
