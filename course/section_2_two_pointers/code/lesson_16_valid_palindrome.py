def pr(val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s = "".join([char for char in s if char.isalnum()])
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            # print("-------------------------")
            # print("left = ", left)
            # print("right = ", right)
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
