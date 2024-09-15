class Solution:
    def numOfArrays(self, length: int, max_val: int, max_cost: int) -> int:
        x = 1000000007
        dp = [[[0] * (max_cost + 1) for _ in range(max_val + 1)] for _ in range(length + 1)]
        for max_value in range(1, max_val + 1):
            dp[1][max_value][1] = 1
        for curr_length in range(2, length + 1):
            for curr_max in range(1, max_val + 1):
                for curr_cost in range(1, max_cost + 1):
                    dp[curr_length][curr_max][curr_cost] = curr_max * dp[curr_length - 1][curr_max][curr_cost] % x
                    for prev_max in range(1, curr_max):
                        dp[curr_length][curr_max][curr_cost] += dp[curr_length - 1][prev_max][curr_cost - 1]
                        dp[curr_length][curr_max][curr_cost] %= x
        result = 0
        for final_max in range(1, max_val + 1):
            result += dp[length][final_max][max_cost]
            result %= x
        return result
