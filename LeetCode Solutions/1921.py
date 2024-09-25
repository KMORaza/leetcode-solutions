from typing import List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [(d / s) for d, s in zip(dist, speed)]
        times.sort()
        count = 0
        for i, t in enumerate(times):
            if t > i:
                count += 1
            else:
                break
        return count
