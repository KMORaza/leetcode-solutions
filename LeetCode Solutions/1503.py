from typing import List
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if not left and not right:
            return 0
        max_left_time = max(left) if left else 0
        max_right_time = max(n - x for x in right) if right else 0
        return max(max_left_time, max_right_time)
