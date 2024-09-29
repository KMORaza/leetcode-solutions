from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        for op in operations:
            if op == "++X" or op == "X++":
                value += 1
            else:
                value -= 1
        return value
