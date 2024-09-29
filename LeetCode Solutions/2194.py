from typing import List
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_col = s[0]
        end_col = s[3]
        start_row = int(s[1])
        end_row = int(s[4])
        result = []
        for col in range(ord(start_col), ord(end_col) + 1):
            for row in range(start_row, end_row + 1):
                result.append(f"{chr(col)}{row}")
        return result
