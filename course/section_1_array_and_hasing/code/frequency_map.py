"""
Given two strings s and t, return True if t is an anagram of s, otherwise False.
Input: s = "anagram", t = "nagaram"
Output: True
Input: s = "rat", t = "car"
Output: False
"""


def test(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq_s = {}
    freq_t = {}
    for ch in s:
        freq_s[ch] = freq_s.get(ch, 0) + 1
    for ch in t:
        freq_t[ch] = freq_t.get(ch, 0) + 1
    return freq_s == freq_t


print("First test should return True")
print(test(s="anagram", t="nagaram"))
print("Second test should return False")
print(test(s="rat", t="car"))
