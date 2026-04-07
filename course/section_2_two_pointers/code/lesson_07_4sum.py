from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        print("nums = ", nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            print("----------------------------------")
            print("i = ", i)
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                print("----------------------")
                print("j = ", j)
                left = j + 1
                right = len(nums) - 1
                print("left = ", left)
                print("right = ", right)
                while left < right:
                    print("-------")
                    print("left = ", left)
                    print("right = ", right)
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    print("sum = ", sum)
                    if sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        print("result = ", result)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
        return result
