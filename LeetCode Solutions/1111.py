from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        depth = 0
        for char in seq:
            if char == '(':
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1
        return result
