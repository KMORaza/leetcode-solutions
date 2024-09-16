from typing import List
class Solution:
    def pathInZigZagTree(self, target: int) -> List[int]:
        depth = 1
        root_val = 1
        while (root_val * 2) <= target:
            root_val *= 2
            depth += 1
        route = []
        for current_depth in range(depth, 0, -1):
            route.append(target)
            level_start = (1 << (current_depth - 1))
            level_end = (1 << current_depth) - 1
            target = (level_start + level_end - target) // 2
        route.reverse()
        return route
