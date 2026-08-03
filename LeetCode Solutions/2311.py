class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        result = 0

        # Count all zeros - they can always be included
        for c in s:
            if c == '0':
                result += 1

        # Try to include as many 1s from right as possible
        val = 0
        power = 1
        ones_added = 0

        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if val + power <= k:
                    val += power
                    ones_added += 1
                else:
                    break
            power *= 2 if i > 0 else 1

        return result + ones_added