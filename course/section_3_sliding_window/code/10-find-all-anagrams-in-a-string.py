from typing import List
from collections import Counter


def pr[T](val: T, title=""):
    print(title, val)
    return val


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        pattern = Counter(p)
        window = Counter(s[:k])
        start = 0
        result = []
        if window == pattern:
            result.append(0)
        for end in range(k, len(s)):
            entering = s[end]
            leaving = s[start]
            window[entering] = window.get(entering, 0) + 1
            window[leaving] -= 1
            if window[leaving] == 0:
                del window[leaving]
            start += 1
            if window == pattern:
                result.append(start)
        return result
