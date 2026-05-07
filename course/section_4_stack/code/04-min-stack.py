def pr[T](val: T, title="") -> T:
    # print(title, val)
    return val


class MinStack:

    def __init__(self):
        self._stack: list[int] = []
        self._min_stack: list[int] = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack:
            self._min_stack.append(val)
        elif self._min_stack[-1] >= val:
            self._min_stack.append(val)
        else:
            self._min_stack.append(self._min_stack[-1])
        # print("------------------")
        # print(self._stack)
        # print(self._min_stack)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int | None:
        return self._min_stack[-1] if self._min_stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
