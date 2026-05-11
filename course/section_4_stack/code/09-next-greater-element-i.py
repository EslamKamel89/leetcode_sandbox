from typing import List


class Solution:
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash = {}
        result = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            nums1_hash[num] = i
        for i in range(len(nums2)):
            if nums2[i] not in nums1_hash:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    result[nums1_hash[nums2[i]]] = nums2[j]
                    break
        return result

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash = {num: i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                val = stack.pop()
                result[nums1_hash[val]] = num
            if num in nums1_hash:
                stack.append(num)
        return result
