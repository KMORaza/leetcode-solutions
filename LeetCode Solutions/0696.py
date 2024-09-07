class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        prev_char = ''
        count = 0
        for char in s:
            if char == prev_char:
                count += 1
            else:
                if prev_char:
                    counts.append(count)
                prev_char = char
                count = 1
        counts.append(count)
        result = 0
        for i in range(1, len(counts)):
            result += min(counts[i-1], counts[i])
        return result
