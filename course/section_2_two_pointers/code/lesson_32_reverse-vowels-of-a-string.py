class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        chars = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
                continue
            left = (left + 1) if chars[left] not in vowels else left
            right = (right - 1) if chars[right] not in vowels else right
        return "".join(chars)
