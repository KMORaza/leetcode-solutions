class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        sequence = [0] * (2 * n - 1)
        self.backtrack(n, 0, 0, sequence)
        return sequence
    def backtrack(self, n: int, index: int, used_mask: int, sequence: list[int]) -> bool:
        if index == len(sequence):
            return True
        if sequence[index] > 0:
            return self.backtrack(n, index + 1, used_mask, sequence)
        for value in range(n, 0, -1):
            if (used_mask >> value) & 1 == 1:
                continue
            if value == 1:
                sequence[index] = value
                if self.backtrack(n, index + 1, used_mask | (1 << value), sequence):
                    return True
                sequence[index] = 0
            else:
                if index + value >= len(sequence) or sequence[index + value] > 0:
                    continue
                sequence[index] = value
                sequence[index + value] = value
                if self.backtrack(n, index + 1, used_mask | (1 << value), sequence):
                    return True
                sequence[index + value] = 0
                sequence[index] = 0
        return False
