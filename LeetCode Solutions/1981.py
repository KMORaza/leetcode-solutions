from typing import List
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        possible_sums = {0}
        for row in mat:
            new_sums = set()
            for num in row:
                for s in possible_sums:
                    new_sums.add(s + num)
            possible_sums = new_sums
        closest_sum = min(possible_sums, key=lambda x: abs(x - target))
        return abs(closest_sum - target)
