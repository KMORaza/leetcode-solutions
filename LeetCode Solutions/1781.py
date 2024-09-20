class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        for i in range(n):
            count = [0] * 26
            max_freq = 0
            for j in range(i, n):
                count[ord(s[j]) - ord('a')] += 1
                max_freq = max(max_freq, count[ord(s[j]) - ord('a')])
                min_freq = min(f for f in count if f > 0)
                total_beauty += max_freq - min_freq
        return total_beauty
