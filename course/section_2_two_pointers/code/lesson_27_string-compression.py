from typing import List


def pr[T](val, title: str = "") -> T:
    print(title, val)
    return val


class Solution:
    def compress1(self, chars: List[str]) -> int:
        s = ""
        i = 0
        while i < len(chars):
            j = i
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            count = j - i
            s = s + chars[i]
            if count > 1:
                s = s + "".join(list(str(count)))
            i = j
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)

    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            group = read
            while group < len(chars) and chars[read] == chars[group]:
                group += 1
            chars[write] = chars[read]
            write += 1
            count = group - read
            if count > 1:
                strs = list(str(count))
                for s in strs:
                    chars[write] = s
                    write += 1
            read = group
        return write
