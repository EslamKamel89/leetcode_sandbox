def pr[T](val: T, debug: bool = True, t: str = "") -> T:
    print(t, val)
    return val


def longest_unique_substring(s):
    start = 0
    substring = ""
    max_len = 0
    for end in range(len(s)):
        substring += s[end]
        while len(substring) != len(set(substring)):
            substring = substring[1:]
            start += 1
        max_len = max(len(substring), max_len)
    return max_len


result = longest_unique_substring("abcabcqbb")
print(result)
