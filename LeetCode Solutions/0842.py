from typing import List
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        output = []
        if self.dfs(num, 0, output):
            return output
        return []
    def dfs(self, num: str, s: int, output: List[int]) -> bool:
        if s == len(num) and len(output) >= 3:
            return True
        for i in range(s, len(num)):
            if num[s] == '0' and i > s:
                break
            val = int(num[s:i+1])
            if val > 2**31 - 1:
                break
            if len(output) >= 2 and val > output[-2] + output[-1]:
                break
            if len(output) <= 1 or val == output[-2] + output[-1]:
                output.append(val)
                if self.dfs(num, i + 1, output):
                    return True
                output.pop()
        return False
