from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: list[int] = []
        for s in operations:
            if s == "+":
                if not stack:
                    raise ValueError("the + operation is called on empty stack")
                elif len(stack) == 1:
                    raise ValueError(
                        "the + operation is called when the stack length is one"
                    )
                else:
                    stack.append(stack[-1] + stack[-2])
            elif s == "D":
                if not stack:
                    raise ValueError("D operations is called on empty stack")
                else:
                    stack.append(stack[-1] * 2)
            elif s == "C":
                if not stack:
                    raise ValueError("C operations is called on empty stack")
                else:
                    stack.pop()
            else:
                val = int(s)
                stack.append(val)
        return sum(stack)
