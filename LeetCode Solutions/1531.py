class Solution:
    def getLengthOfOptimalCompression(self, data: str, limit: int) -> int:
        size = len(data)
        dp = [[101] * (limit + 1) for _ in range(size)]
        return self.findOptimalCompression(data, 0, limit, dp)
    def findOptimalCompression(self, sequence: str, position: int, remainingDeletions: int, dp: list[list[int]]) -> int:
        if remainingDeletions < 0:
            return 101
        if position == len(sequence) or len(sequence) - position <= remainingDeletions:
            return 0
        if dp[position][remainingDeletions] != 101:
            return dp[position][remainingDeletions]
        highestCount = 0
        charCount = [0] * 128
        for end in range(position, len(sequence)):
            highestCount = max(highestCount, charCount[ord(sequence[end])] + 1)
            charCount[ord(sequence[end])] += 1
            dp[position][remainingDeletions] = min(
                dp[position][remainingDeletions],
                self.determineLength(highestCount) + self.findOptimalCompression(sequence, end + 1, remainingDeletions - (end - position + 1 - highestCount), dp))
        return dp[position][remainingDeletions]
    def determineLength(self, highestCount: int) -> int:
        if highestCount == 1:
            return 1
        if highestCount < 10:
            return 2
        if highestCount < 100:
            return 3
        return 4