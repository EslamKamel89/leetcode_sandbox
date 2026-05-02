from typing import List


def pr[T](val: T, debug=True):
    if debug:
        print(val)
    return val


class Solution:
    def minSubArrayLen1(self, target: int, nums: List[int]) -> int | float:
        min_len = float("inf")
        for i in range(len(nums)):
            current_sum = nums[i]
            if current_sum >= target:
                return 1
            for j in range(i + 1, len(nums)):
                current_sum += nums[j]
                if current_sum >= target:
                    min_len = min(min_len, j - i + 1)
                    break
        return min_len if min_len != float("inf") else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int | float:
        start, total = 0, 0
        result = float("inf")
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                result = min(result, end - start + 1)
                total -= nums[start]
                start += 1

        return result if result != float("inf") else 0
