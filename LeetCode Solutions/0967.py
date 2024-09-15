from typing import List
from collections import deque
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        result = []
        queue = deque(range(1, 10))
        while queue:
            num = queue.popleft()
            if len(str(num)) == n:
                result.append(num)
                continue
            last_digit = num % 10
            if last_digit + k < 10:
                queue.append(num * 10 + (last_digit + k))
            if k > 0 and last_digit - k >= 0:
                queue.append(num * 10 + (last_digit - k))
        return result
