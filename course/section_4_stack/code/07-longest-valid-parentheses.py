def pr[T](val: T, title="") -> T:
    # print(title, val)
    return val


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        stack = [[")", -1]]
        if not s:
            return 0
        for i, char in enumerate(s):
            stack.append([char, i])
            while len(stack) >= 2 and stack[-1][0] == ")" and stack[-2][0] == "(":
                stack.pop()
                stack.pop()
        stack.append([")", len(s)])
        mx = 0
        prev = 0
        for _, i in stack:
            mx = max(mx, i - prev - 1)
            prev = i
        return mx
    
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
