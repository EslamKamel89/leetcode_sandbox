def has_anagram_substring(s: str, pattern: str):
    k = len(pattern)
    pattern_set = set(pattern)
    window_set = set(s[:k])
    if pattern_set == window_set:
        return True
    for i in range(k, len(s)):
        window_set.add(s[i])
        window_set.remove(s[i - k])
        if window_set == pattern_set:
            return True
    return False


result = has_anagram_substring("greyhounds", "hoy")
print(result)
result = has_anagram_substring("gruyheonds", "hoy")
print(result)
