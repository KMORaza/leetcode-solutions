class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s * 2
        pattern1 = ''.join('01'[(i % 2)] for i in range(n * 2))
        pattern2 = ''.join('10'[(i % 2)] for i in range(n * 2))
        count1 = [0] * (n * 2 + 1)
        count2 = [0] * (n * 2 + 1)
        for i in range(1, n * 2 + 1):
            count1[i] = count1[i - 1] + (s[i - 1] != pattern1[i - 1])
            count2[i] = count2[i - 1] + (s[i - 1] != pattern2[i - 1])
        min_flips = float('inf')
        for i in range(n, n * 2 + 1):
            min_flips = min(min_flips, count1[i] - count1[i - n], count2[i] - count2[i - n])
        return min_flips
