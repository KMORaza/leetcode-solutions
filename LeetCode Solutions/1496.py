class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited_positions = set()
        x, y = 0, 0
        visited_positions.add((x, y))
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            if (x, y) in visited_positions:
                return True
            visited_positions.add((x, y))
        return False
