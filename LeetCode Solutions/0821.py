from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [float('inf')] * n
        closest = float('inf')
        for i in range(n):
            if s[i] == c:
                closest = i
            answer[i] = min(answer[i], abs(i - closest))
        closest = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                closest = i
            answer[i] = min(answer[i], abs(i - closest))
        return answer
