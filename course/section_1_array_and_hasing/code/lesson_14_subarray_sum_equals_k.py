from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        mp = {0: 1}
        print("nums = ", nums)
        for x in nums:
            prefix += x
            print(f"......... {x} ............")
            print("prefix = ", prefix)
            print("prefix - k = ", prefix - k)
            if prefix - k in mp:
                count += mp[prefix - k]
            print("count = ", count)
            mp[prefix] = mp.get(prefix, 0) + 1
            print("mp= ", mp)
        return count
