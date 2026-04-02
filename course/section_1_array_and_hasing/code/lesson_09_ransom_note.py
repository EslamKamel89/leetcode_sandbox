class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_r: dict[str, int] = {}
        freq_m: dict[str, int] = {}
        for char in ransomNote:
            freq_r[char] = freq_r.get(char, 0) + 1
        for char in magazine:
            freq_m[char] = freq_m.get(char, 0) + 1
        for char, freq in freq_r.items():
            if freq_m.get(char, 0) < freq:
                return False
        return True


res = Solution().canConstruct(ransomNote="aa", magazine="aab")
print(res)
