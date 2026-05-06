from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        prefix[i:j] % k = 0
        prefix[i] % k - prefix[i] % k = 0
        prefix[i] % k  = prefix[j] % k
        """
        if len(nums) < 2:
            return False
        if k == 1:
            return True
        seen = {0: -1}
        prefix_sum = 0
        # print('nums = ' , nums)
        for i, num in enumerate(nums):
            # print('---------------------------')
            # print('i = ' , i )
            # print('num = ' , num)
            prefix_sum += num
            rem = prefix_sum % k
            # print('prefix_sum = ' , prefix_sum)
            # print('rem = ' , rem )
            if rem not in seen:
                seen[rem] = i
            elif i - seen[rem] > 1:
                return True

        return False
