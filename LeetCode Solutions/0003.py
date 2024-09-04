class Solution:
    def lengthOfLongestSubstring(self, s):
        seen_chars = set()
        start = 0
        max_length = 0
        for end in range(len(s)):
            while s[end] in seen_chars:
                seen_chars.remove(s[start])
                start += 1
            seen_chars.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length
