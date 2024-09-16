from typing import List
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        result = [[0] * len(colsum) for _ in range(2)]
        for i, val in enumerate(colsum):
            if val == 2:
                if upper > 0 and lower > 0:
                    result[0][i] = result[1][i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []
        for i, val in enumerate(colsum):
            if val == 1:
                if upper > lower:
                    if upper > 0:
                        result[0][i] = 1
                        upper -= 1
                    else:
                        return []
                else:
                    if lower > 0:
                        result[1][i] = 1
                        lower -= 1
                    else:
                        return []
        if upper != 0 or lower != 0:
            return []
        return result
