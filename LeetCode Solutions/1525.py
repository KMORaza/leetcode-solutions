class Solution:
    def numSplits(self, s: str) -> int:
        left_count = [0] * 26
        right_count = [0] * 26
        unique_left = 0
        unique_right = 0
        for char in s:
            if right_count[ord(char) - ord('a')] == 0:
                unique_right += 1
            right_count[ord(char) - ord('a')] += 1
        result = 0
        for char in s:
            if left_count[ord(char) - ord('a')] == 0:
                unique_left += 1
            left_count[ord(char) - ord('a')] += 1
            if right_count[ord(char) - ord('a')] == 1:
                unique_right -= 1
            right_count[ord(char) - ord('a')] -= 1
            if unique_left == unique_right:
                result += 1
        return result
