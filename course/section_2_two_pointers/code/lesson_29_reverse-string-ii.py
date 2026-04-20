def pr[T](val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def reverse_range(self, s: list[str], start: int, end: int) -> str:
        # assert start <= end
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return "".join(s)

    def reverseStr1(self, s: str, k: int) -> str:
        if k >= len(s):
            return self.reverse_range(list(s), 0, len(s) - 1)
        i = 0
        reverse = True
        while i <= len(s):
            if reverse:
                reverse = False
                s = self.reverse_range(list(s), i, min(i + k - 1, len(s) - 1))
            else:
                reverse = True
            i += k
        return s

    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
        for i in range(0, n, 2 * k):
            print("-----------------")
            print("i = ", i)
            left = i
            right = min(i + k - 1, n - 1)
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
