from typing import List
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        count = 0
        last_rung = 0
        for rung in rungs:
            if rung - last_rung > dist:
                count += (rung - last_rung - 1) // dist
            last_rung = rung
        return count
