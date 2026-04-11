from typing import List


def pr(val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m, m + n):
            nums1[i] = nums2[i - m]
        nums1.sort()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
