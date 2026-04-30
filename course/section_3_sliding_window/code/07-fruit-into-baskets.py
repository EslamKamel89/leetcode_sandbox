from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq = {}
        left, total, max_count = 0, 0, 0
        for right in range(len(fruits)):
            entering = fruits[right]
            freq[entering] = freq.get(entering, 0) + 1
            total += 1
            while len(freq) > 2:
                leaving = fruits[left]
                freq[leaving] -= 1
                left += 1
                total -= 1
                if freq[leaving] == 0:
                    del freq[leaving]
            max_count = max(max_count, total)
        return max_count
