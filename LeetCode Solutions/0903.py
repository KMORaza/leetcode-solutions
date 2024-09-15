class Solution:
    def numPermsDISequence(self, s: str) -> int:
        k = 1_000_000_007
        x = len(s)
        dp = [[0] * (x + 1) for _ in range(x + 1)]
        for j in range(x + 1):
            dp[0][j] = 1
        for i in range(1, x + 1):
            if s[i - 1] == 'I':
                postfix_sum = 0
                for j in range(x - i, -1, -1):
                    postfix_sum = (postfix_sum + dp[i - 1][j + 1]) % k
                    dp[i][j] = postfix_sum
            else:
                prefix_sum = 0
                for j in range(x - i + 1):
                    prefix_sum = (prefix_sum + dp[i - 1][j]) % k
                    dp[i][j] = prefix_sum
        return dp[x][0]
