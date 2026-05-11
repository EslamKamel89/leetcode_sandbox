class StockSpanner:

    def __init__(self):
        self.stack: list[list[int]] = []  # [[price , span]]

    def next(self, price: int) -> int:
        new_span = 1
        if not self.stack or price < self.stack[-1][0]:
            self.stack.append([price, 1])
            # print('---')
            # print(self.stack)
            return new_span
        while self.stack and self.stack[-1][0] <= price:
            new_span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, new_span])
        # print(self.stack)
        return new_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
