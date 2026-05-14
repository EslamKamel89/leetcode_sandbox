class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = []
                while stack and stack[-1] != "[":
                    popped = stack.pop()
                    temp.insert(0, popped)
                stack.pop()
                multiplier = ""
                while stack and stack[-1] in "0123456789":
                    popped = stack.pop()
                    multiplier = popped + multiplier
                # print(multiplier)
                stack += temp * int(multiplier)
        return "".join(stack)
