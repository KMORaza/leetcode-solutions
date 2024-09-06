class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def longest_substring_helper(s: str, k: int) -> int:
            if len(s) < k:
                return 0
            from collections import Counter
            freq = Counter(s)
            for char, count in freq.items():
                if count < k:
                    return max(longest_substring_helper(subs, k) for subs in s.split(char))
            return len(s)
        return longest_substring_helper(s, k)
