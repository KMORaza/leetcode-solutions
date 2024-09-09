class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        cumulative_shifts = [0] * n
        cumulative_shifts[n-1] = shifts[n-1]
        for i in range(n-2, -1, -1):
            cumulative_shifts[i] = cumulative_shifts[i+1] + shifts[i]
        result = list(s)
        for i in range(n):
            new_char = chr((ord(result[i]) - ord('a') + cumulative_shifts[i]) % 26 + ord('a'))
            result[i] = new_char
        return ''.join(result)
