class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 2:
            return stones[1] - stones[0]

        max_jump = 0

        for i in range(2, n):
            max_jump = max(max_jump, stones[i] - stones[i - 2])

        max_jump = max(max_jump, stones[n - 1] - stones[n - 2])

        return max_jump