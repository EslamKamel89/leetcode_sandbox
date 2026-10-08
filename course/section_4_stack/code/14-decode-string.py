class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                mult = ""
                while stack and stack[-1].isnumeric():
                    mult = stack.pop() + mult
                stack.append(int(mult) * temp)
        return "".join(stack)
