class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        s = s.replace(" ", "") + "+"
        stack, current_num, operator = [], 0, "+"
        all_operators = {"+", "-", "*", "/"}
        for i, token in enumerate(s):
            if token.isdigit():
                current_num = current_num * 10 + int(token)
            else:
                if operator == "+":
                    stack.append(current_num)
                elif operator == "-":
                    stack.append(-current_num)
                elif operator == "*":
                    stack.append(stack.pop() * current_num)
                elif operator == "/":
                    stack.append(int(stack.pop() / current_num))
                current_num = 0
                operator = token
        return sum(stack)
