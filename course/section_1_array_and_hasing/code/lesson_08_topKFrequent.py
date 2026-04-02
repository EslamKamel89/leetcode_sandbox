from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for num in nums:
            groups[num] = groups.get(num, 0) + 1
        # print(groups)
        result = sorted([g for g in groups.items()], key=lambda x: x[1], reverse=True)
        result = [g[0] for g in result]
        return list(result[:k])
