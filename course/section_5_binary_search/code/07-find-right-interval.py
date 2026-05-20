from typing import List


def pr[T](val: T, title="") -> T:
    print(title, val)
    return val


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = []
        for i, interval in enumerate(intervals):
            starts.append((interval[0], i))
        starts.sort(key=lambda x: x[0])
        res = [-1] * len(intervals)
        for i, (start, end) in enumerate(intervals):
            l, r = 0, len(intervals) - 1
            ans = -1
            while l <= r:
                m = (l + r) // 2
                if starts[m][0] >= end:
                    ans = starts[m][1]
                    r = m - 1
                else:
                    l = m + 1
            res[i] = ans
        return res
