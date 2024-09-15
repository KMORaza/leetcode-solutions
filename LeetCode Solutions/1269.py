class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        max_pos = min(steps, arrLen - 1)
        prev = [0] * (max_pos + 1)
        curr = [0] * (max_pos + 1)
        prev[0] = 1
        for i in range(1, steps + 1):
            for j in range(max_pos + 1):
                curr[j] = prev[j]
                if j > 0:
                    curr[j] = (curr[j] + prev[j - 1]) % MOD
                if j < max_pos:
                    curr[j] = (curr[j] + prev[j + 1]) % MOD
            prev, curr = curr, prev
        return prev[0]

