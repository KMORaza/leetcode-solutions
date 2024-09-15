from typing import List
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        odd_part = self.beautifulArray((n + 1) // 2)
        even_part = self.beautifulArray(n // 2)
        result = []
        for num in odd_part:
            result.append(2 * num - 1)
        for num in even_part:
            result.append(2 * num)
        return result
