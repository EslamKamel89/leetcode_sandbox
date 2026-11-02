from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = {0: 1}
        prefix, res = 0, 0
        for num in nums:
            prefix += num
            rem = prefix - k
            if rem in prefixes:
                res += prefixes[rem]
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
        return res
