from typing import List


class Solution:
    # solution one
    # def containsDuplicate_1(self, nums: List[int]) -> bool:
    #     unique = set(nums)
    #     return len(unique) != len(nums)
    # solution two
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


res = Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
print(res)
