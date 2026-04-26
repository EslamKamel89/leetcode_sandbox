def count_anagram_substrings(s: str, pattern: str):
    k = len(pattern)
    pattern_freq = {}
    for char in pattern:
        pattern_freq[char] = pattern_freq.get(char, 0) + 1
    window_freq = {}
    for char in s[:k]:
        window_freq[char] = window_freq.get(char, 0) + 1
    count = 0
    if pattern_freq == window_freq:
        count += 1
    for i in range(k, len(s)):
        window_freq[s[i]] = window_freq.get(s[i], 0) + 1
        window_freq[s[i - k]] -= 1
        if window_freq[s[i - k]] == 0:
            del window_freq[s[i - k]]
        if window_freq == pattern_freq:
            count += 1
    return count


result = count_anagram_substrings(s="gattactat", pattern="att")
print(result)
