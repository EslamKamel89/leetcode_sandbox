from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for read in range(1, len(nums)):
            print(f"----------------------")
            print("nums = ", nums)
            print("read = ", read)
            print("write = ", write)
            print("nums[read] = ", nums[read])
            print("nums[write] = ", nums[write])
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
            print("nums = ", nums)
            print("write = ", write)
        return write
