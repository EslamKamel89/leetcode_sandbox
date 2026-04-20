from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest = 0
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        for i in range(len(arr) - 1):
            if arr[i] == x or (arr[i] < x and arr[i + 1] > x):
                closest = i if abs(arr[i] - x) < abs(arr[i + 1] - x) else i + 1
                break
        left = closest
        right = closest + 1
        while (right - left) < k:
            if left == 0:
                right += 1
            elif right == len(arr):
                left -= 1
            else:
                if abs(arr[left - 1] - x) > abs(arr[right] - x):
                    right += 1
                else:
                    left -= 1

        return arr[left:right]
