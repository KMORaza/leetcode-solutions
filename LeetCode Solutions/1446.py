class Solution:
    def maxPower(self, s: str) -> int:
        max_length = 0
        current_length = 0
        prev_char = None
        for char in s:
            if char == prev_char:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
                prev_char = char
        max_length = max(max_length, current_length)
        return max_length
