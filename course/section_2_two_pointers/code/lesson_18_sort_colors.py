from typing import List


def pr(val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def sortColors1(self, nums: List[int]) -> None:
        nums.sort()

    def sortColors2(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            # print("-------------------------------")
            # print("nums = ", nums)
            # print("i = ", i)
            # print("nums[i] = ", nums[i])
            # print("left = ", left)
            # print("nums[left]", nums[left])
            # print("right = ", right)
            # print("nums[right] = ", nums[right])
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            elif nums[i] == 1:
                i += 1
            # print("nums = ", nums)

    def sortColors3(self, nums: List[int]) -> None:
        freq = [0, 0, 0]
        for num in nums:
            if num == 0:
                freq[0] += 1
            if num == 1:
                freq[1] += 1
            if num == 2:
                freq[2] += 1
        for i in range(len(nums)):
            if freq[0] != 0:
                nums[i] = 0
                freq[0] -= 1
            elif freq[1] != 0:
                nums[i] = 1
                freq[1] -= 1
            elif freq[2] != 0:
                nums[i] = 2
                freq[2] -= 1

    def sortColors(self, nums: List[int]) -> None:
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        for i in range(left, len(nums)):
            if nums[i] == 1:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
