from typing import List


def pr[T](val: T, title="") -> T:
    # print(title, val)
    return val


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if pushed == popped:
            return True
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack
