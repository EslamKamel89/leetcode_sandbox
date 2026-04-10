from typing import List


class Solution:
    def trap1(self, height: List[int]) -> int:
        if not height:
            return 0
        data: dict[int, dict[str, int]] = {}
        max_left = 0
        max_right = 0
        water = 0
        for i in range(len(height)):
            if i > 0:
                max_left = max(max_left, height[i - 1])
            data[i] = {"max_left": max_left}
        for j in reversed(range(len(height))):
            if j < len(height) - 1:
                max_right = max(max_right, height[j + 1])
            new_water = min(data[j]["max_left"], max_right) - height[j]
            new_water = max(0, new_water)
            water += new_water
        return water

    def trap2(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        max_l = height[0]
        max_r = height[-1]
        water = 0
        while left < right:
            # print("-------------------------")
            max_l = max(max_l, height[left])
            max_r = max(max_r, height[right])
            # print("max_l = ", max_l)
            # print("max_r = ", max_r)
            if max_l < max_r:
                left += 1
                new_water = max_l - height[left]
                # print("new_water = ", new_water)
                if new_water > 0:
                    water += new_water
            else:
                right -= 1
                new_water = max_r - height[right]
                # print("new_water = ", new_water)
                if new_water > 0:
                    water += new_water
        return water

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_l, max_r = height[left], height[right]
        water = 0
        while left < right:
            if max_l < max_r:
                left += 1
                max_l = max(max_l, height[left])
                new_water = max_l - height[left]
                if new_water > 0:
                    water += new_water
            else:
                right -= 1
                max_r = max(max_r, height[right])
                new_water = max_r - height[right]
                if new_water > 0:
                    water += new_water
        return water
