from typing import List


def pr[T](val: T, title="") -> T:
    print(title, val)
    return val


class Solution:
    def dailyTemperatures1(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack: list[list[int]] = []  # [[temp , index]]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_i = stack.pop()
                result[stack_i] = i - stack_i
            stack.append([temp, i])
        return result
