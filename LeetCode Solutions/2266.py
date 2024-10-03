class Solution:
    def countTexts(self, keySequence: str) -> int:
        x = 10**9+7
        sequence_length = len(keySequence)
        combinations = [0] * (sequence_length + 1)
        combinations[sequence_length] = 1
        for position in range(sequence_length - 1, -1, -1):
            combinations[position] = combinations[position + 1]
            if self.hasSameDigits(keySequence, position, 2):
                combinations[position] += combinations[position + 2]
            if self.hasSameDigits(keySequence, position, 3):
                combinations[position] += combinations[position + 3]
            if keySequence[position] in '79' and self.hasSameDigits(keySequence, position, 4):
                combinations[position] += combinations[position + 4]
            combinations[position] %= x
        return combinations[0]
    def hasSameDigits(self, text: str, startIndex: int, countDigits: int) -> bool:
        if startIndex + countDigits > len(text):
            return False
        for idx in range(startIndex + 1, startIndex + countDigits):
            if text[idx] != text[startIndex]:
                return False
        return True