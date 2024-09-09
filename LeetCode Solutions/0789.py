class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        distance_to_target = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            distance_to_target_from_ghost = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if distance_to_target_from_ghost <= distance_to_target:
                return False
        return True
