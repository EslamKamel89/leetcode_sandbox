from typing import List
from math import floor, ceil


class Solution:
    def round_to_zero(self, n: float) -> int:
        if n >= 0:
            return floor(n)
        return ceil(n)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(self.round_to_zero(num1 / num2))
        return stack[0]
