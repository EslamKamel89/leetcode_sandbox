from typing import List


def pr(val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def meeting_point(self, nums: list[int]) -> int | None:
        slow = 0
        fast = 0
        while True:
            # print("------------------------------")
            # print("slow = ", slow)
            # print("fast = ", fast)
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                return slow
        return None

    def findDuplicate(self, nums: List[int]) -> int:
        meeting = self.meeting_point(nums)
        if meeting == None:
            return -1
        print("meeting = ", meeting)
        current = 0
        while current != meeting:
            meeting = nums[meeting]
            current = nums[current]
        return current

    def findDuplicate2(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
