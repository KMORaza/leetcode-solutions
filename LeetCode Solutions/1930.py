class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        count = 0
        for char in first_occurrence:
            if first_occurrence[char] < last_occurrence[char]:
                unique_chars = set(s[first_occurrence[char] + 1:last_occurrence[char]])
                count += len(unique_chars)
        return count
