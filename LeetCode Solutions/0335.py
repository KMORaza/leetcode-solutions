class Solution:
    def isSelfCrossing(self, distance):
        visited = set()
        x, y = 0, 0
        visited.add((x, y))
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        direction_index = 0
        for d in distance:
            dx, dy = directions[direction_index]
            for _ in range(d):
                x += dx
                y += dy
                if (x, y) in visited:
                    return True
                visited.add((x, y))
            direction_index = (direction_index + 1) % 4
        return False
