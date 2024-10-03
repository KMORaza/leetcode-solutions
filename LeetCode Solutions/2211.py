class Solution:
    def countCollisions(self, directions: str) -> int:
        total_collisions = 0
        start_index = 0
        end_index = len(directions) - 1
        while start_index < len(directions) and directions[start_index] == 'L':
            start_index += 1
        while end_index >= 0 and directions[end_index] == 'R':
            end_index -= 1
        for current_position in range(start_index, end_index + 1):
            if directions[current_position] != 'S':
                total_collisions += 1
        return total_collisions
