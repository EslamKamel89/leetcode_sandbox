class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        freq: dict[str, int] = {}
        start, max_len = 0, 0
        for end in range(len(s)):
            entering = s[end]
            freq[entering] = freq.get(entering, 0) + 1
            while len(freq) > k:
                leaving = s[start]
                freq[leaving] -= 1
                if freq[leaving] == 0:
                    del freq[leaving]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
