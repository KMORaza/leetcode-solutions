class Solution:
    def sumScores(self, text: str) -> int:
        str_length = len(text)
        z_values = [0] * str_length
        start, end = 0, 0
        for pos in range(1, str_length):
            if pos < end:
                z_values[pos] = min(end - pos, z_values[pos - start])
            while pos + z_values[pos] < str_length and text[z_values[pos]] == text[pos + z_values[pos]]:
                z_values[pos] += 1
            if pos + z_values[pos] > end:
                start = pos
                end = pos + z_values[pos]
        return sum(z_values) + str_length