from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
         subarray[i:j] % k = 0
        ( prefix[i] - prefix[j] ) % k = 0
         prefix[i] % k - prefix[j] % k = 0
         prefix[i] % k  = prefix[j] % k
        """
        print("nums = ", nums)
        seen: dict[int, int] = {}
        sum = 0
        for i, num in enumerate(nums):
            print(f" ---------------- {i} ---------------- ")
            sum += num
            rem = sum % k
            print("sum = ", sum)
            print("rem = ", rem)
            if rem in seen:
                return True
            seen[sum % k] = i

        print("seen = ", seen)
        return False
