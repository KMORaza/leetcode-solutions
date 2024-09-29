class Solution:
    def placeWordInCrossword(self, puzzle, phrase):
        for layout in [puzzle, self.rotate_puzzle(puzzle)]:
            for row in layout:
                for fragment in ''.join(row).split('#'):
                    for option in [phrase, phrase[::-1]]:
                        if len(option) == len(fragment):
                            if self.can_place(option, fragment):
                                return True
        return False
    def rotate_puzzle(self, puzzle):
        height = len(puzzle)
        width = len(puzzle[0])
        rotated_structure = [[''] * height for _ in range(width)]
        for r in range(height):
            for c in range(width):
                rotated_structure[c][r] = puzzle[r][c]
        return rotated_structure
    def can_place(self, option, fragment):
        for idx in range(len(option)):
            if fragment[idx] != ' ' and fragment[idx] != option[idx]:
                return False
        return True
