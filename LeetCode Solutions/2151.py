from typing import List
class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        for mask in range(1 << n):
            valid = True
            good_count = 0
            for i in range(n):
                if mask & (1 << i):
                    good_count += 1
                    for j in range(n):
                        if statements[i][j] == 1 and not (mask & (1 << j)):
                            valid = False
                        elif statements[i][j] == 0 and (mask & (1 << j)):
                            valid = False
            if valid:
                max_good = max(max_good, good_count)
        return max_good