def pr[T](val: T, debug: bool = True) -> T:
    if debug:
        print(val)
    return val


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_window = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in current_window:
                current_window.remove(s[left])
                left += 1
            current_window.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
