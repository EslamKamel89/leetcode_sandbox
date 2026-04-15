from math import ceil, sqrt


def pr[T](val, title: str = ""):
    print(title, val)
    return val


class Solution:
    def judgeSquareSum1(self, c: int) -> bool:
        if c == 0:
            return True
        for i in range(c + 1):
            for j in range(c + 1):
                if (i**2) + (j**2) == c:
                    return True
        return False

    def judgeSquareSum2(self, c: int) -> bool:
        if c == 0:
            return True
        end = ceil(c**0.5) + 1
        print("end = ", end)
        for i in range(end):
            # print('-----------------------')
            # print('i = ' , i)
            for j in range(end):
                # print('-------')
                # print('j = ' , j)
                if (i**2) + (j**2) == c:
                    return True
        return False

    def judgeSquareSum3(self, c: int) -> bool:
        squares = set()
        for i in range(int(sqrt(c)) + 1):
            squares.add(i * i)
        for i in range(int(sqrt(c)) + 1):
            target = c - (i * i)
            if target in squares:
                return True
        return False

    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        left = 0
        right = int(sqrt(c))
        while left <= right:
            # print("--------------------------")
            # print("left = ", left)
            # print("right = ", right)
            squares_sum = (left**2) + (right**2)
            if c == squares_sum:
                return True
            elif c < squares_sum:
                right -= 1
            elif c > squares_sum:
                left += 1
        return False
