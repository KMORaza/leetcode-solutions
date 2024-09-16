class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, direction_index = 0, 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x += directions[direction_index][0]
                y += directions[direction_index][1]
            elif instruction == 'L':
                direction_index = (direction_index - 1) % 4
            elif instruction == 'R':
                direction_index = (direction_index + 1) % 4
        return (x == 0 and y == 0) or direction_index != 0
