from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            freq = {}
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            count = 0
            for s in freq.values():
                if s > 1:
                    count += 1
            return count
        count = 0
        unique = set(nums)
        for num in unique:
            if num + k in unique:
                count += 1
        return count
