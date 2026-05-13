class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return "0"
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        stack = stack[: len(stack) - k]
        while stack and stack[0] == "0":
            stack.pop(0)
        res = "".join(stack)
        return res if res else "0"
