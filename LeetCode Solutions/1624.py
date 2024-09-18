class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indices = {}
        max_length = -1
        for index, char in enumerate(s):
            if char in char_indices:
                length = index - char_indices[char] - 1
                max_length = max(max_length, length)
            else:
                char_indices[char] = index
        return max_length
