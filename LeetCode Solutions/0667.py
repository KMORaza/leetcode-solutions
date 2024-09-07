from typing import List
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = []
        for i in range(1, k + 2):
            if i % 2 == 1:
                result.append((i + 1) // 2)
            else:
                result.append(k + 2 - (i // 2))
        for i in range(k + 2, n + 1):
            result.append(i)
        return result
