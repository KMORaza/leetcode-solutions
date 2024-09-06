class Solution:
    def canCross(self, stones: list[int]) -> bool:
        dp = {}
        dp[stones[0]] = {0}
        for stone in stones:
            if stone not in dp:
                continue
            for jump in dp[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0:
                        next_stone = stone + next_jump
                        if next_stone in dp:
                            dp[next_stone].add(next_jump)
                        else:
                            dp[next_stone] = {next_jump}
        return stones[-1] in dp