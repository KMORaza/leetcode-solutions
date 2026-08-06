class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(types)

        dp = [0] * (target + 1)
        dp[0] = 1

        for count, marks in types:
            new_dp = dp[:]
            for t in range(target + 1):
                for k in range(1, min(count, t // marks) + 1):
                    new_dp[t] = (new_dp[t] + dp[t - k * marks]) % MOD
            dp = new_dp

        return dp[target]