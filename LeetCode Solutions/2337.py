class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        start_pieces = []
        target_pieces = []

        for i in range(n):
            if start[i] != '_':
                start_pieces.append((start[i], i))
            if target[i] != '_':
                target_pieces.append((target[i], i))

        if len(start_pieces) != len(target_pieces):
            return False

        for i in range(len(start_pieces)):
            start_char, start_pos = start_pieces[i]
            target_char, target_pos = target_pieces[i]

            if start_char != target_char:
                return False

            if start_char == 'L' and start_pos < target_pos:
                return False

            if start_char == 'R' and start_pos > target_pos:
                return False

        return True