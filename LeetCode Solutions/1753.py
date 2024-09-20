class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones = [a, b, c]
        stones.sort(reverse=True)
        score = 0
        while stones[1] > 0:
            stones[0] -= 1
            stones[1] -= 1
            score += 1
            stones.sort(reverse=True)
        return score
