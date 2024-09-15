class Solution:
    def longestAwesome(self, s: str) -> int:
        first_occurrence = {0: -1}
        mask = 0
        max_length = 0
        for i, char in enumerate(s):
            digit = int(char)
            mask ^= (1 << digit)
            if mask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[mask])
            else:
                first_occurrence[mask] = i
            for j in range(10):
                altered_mask = mask ^ (1 << j)
                if altered_mask in first_occurrence:
                    max_length = max(max_length, i - first_occurrence[altered_mask])
        return max_length
