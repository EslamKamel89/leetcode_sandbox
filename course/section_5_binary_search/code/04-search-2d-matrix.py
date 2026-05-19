from typing import List


def pr[T](val: T, title="") -> T:
    print(title, val)
    return val


class Solution:
    def binary_search(self, nums: list[int], target) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            m = (bottom + top) // 2
            row = matrix[m]
            if row[0] > target:
                bottom = m - 1
            elif row[-1] < target:
                top = m + 1
            else:
                return self.binary_search(row, target)
        return False
