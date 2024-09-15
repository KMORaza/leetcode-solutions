class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        from collections import defaultdict
        def get_bitmask(word):
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - ord('a'))
            return bitmask
        word_count = defaultdict(int)
        for word in words:
            bitmask = get_bitmask(word)
            word_count[bitmask] += 1
        result = []
        for puzzle in puzzles:
            puzzle_mask = get_bitmask(puzzle)
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            count = 0
            submask = puzzle_mask
            while submask:
                if (submask & first_char_mask) and submask in word_count:
                    count += word_count[submask]
                submask = (submask - 1) & puzzle_mask
            result.append(count)
        return result
