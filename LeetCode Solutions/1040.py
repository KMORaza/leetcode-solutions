class Solution:
    def numMovesStonesII(self, positions):
        length = len(positions)
        min_moves_required = length
        positions.sort()
        start = 0
        for end in range(length):
            while positions[end] - positions[start] + 1 > length:
                start += 1
            stones_in_window = end - start + 1
            if stones_in_window == length - 1 and positions[end] - positions[start] + 1 == length - 1:
                min_moves_required = min(min_moves_required, 2)
            else:
                min_moves_required = min(min_moves_required, length - stones_in_window)
        return [
            min_moves_required,
            max(positions[length - 1] - positions[1] - length + 2, positions[length - 2] - positions[0] - length + 2)
        ]
