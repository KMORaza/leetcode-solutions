from typing import List
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        x, y = startPos
        result = []
        for i in range(len(s)):
            steps = 0
            cx, cy = x, y
            for j in range(i, len(s)):
                if s[j] == 'U':
                    cx -= 1
                elif s[j] == 'D':
                    cx += 1
                elif s[j] == 'L':
                    cy -= 1
                elif s[j] == 'R':
                    cy += 1
                if 0 <= cx < n and 0 <= cy < n:
                    steps += 1
                else:
                    break
            result.append(steps)
        return result
