class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        open_to_close = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in open_to_close:
                if stack and stack[-1] == open_to_close[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
