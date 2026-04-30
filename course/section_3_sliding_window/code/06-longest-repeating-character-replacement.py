def pr[T](val: T, debug=True):
    if debug:
        print(val)
    return val


class Solution:
    def find_max(self, freq: dict[str, int]) -> int:
        max_freq = 0
        for f in freq.values():
            max_freq = max(f, max_freq)
        return max_freq

    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        window: dict[str, int] = {}
        max_len = 0
        for end in range(len(s)):
            entering = s[end]
            window[entering] = window.get(entering, 0) + 1
            while (end - start + 1 - self.find_max(window)) > k:
                leaving = s[start]
                window[leaving] -= 1
                start += 1
                # if window[leaving] == 0:
                #     del window[leaving]
            max_len = max(max_len, end - start + 1)
        return max_len
