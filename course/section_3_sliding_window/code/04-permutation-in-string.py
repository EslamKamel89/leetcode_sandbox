from collections import Counter


def pr[T](val: T, debug=True) -> T:
    if debug:
        print(val)
    return val


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        k = len(s1)
        current_window = Counter(s2[:k])
        if pattern == current_window:
            return True
        for i in range(k, len(s2)):
            entering = s2[i]
            leaving = s2[i - k]
            current_window[entering] = current_window.get(entering, 0) + 1
            current_window[leaving] = current_window.get(leaving) - 1  # type: ignore
            if current_window[leaving] == 0:
                del current_window[leaving]
            if pattern == current_window:
                return True

        return False
