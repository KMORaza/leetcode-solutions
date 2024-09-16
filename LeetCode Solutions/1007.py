from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def count_rotations(target: int) -> int:
            top_rotations = bottom_rotations = 0
            for top, bottom in zip(tops, bottoms):
                if top != target and bottom != target:
                    return float('inf')
                elif top != target:
                    top_rotations += 1
                elif bottom != target:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)
        result = min(count_rotations(tops[0]), count_rotations(bottoms[0]))
        return result if result != float('inf') else -1
