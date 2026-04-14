def pr[T](val: T, title: str = "") -> T:
    print(title, val)
    print("")
    return val


class Solution:
    def is_valid_palindrome_range(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.is_valid_palindrome_range(
                    s, left + 1, right
                ) or self.is_valid_palindrome_range(s, left, right - 1)
            left += 1
            right -= 1

        return True
