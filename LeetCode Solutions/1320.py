class Solution:
    def minimumDistance(self, text: str) -> int:
        dp = [[[None for _ in range(len(text))] for _ in range(27)] for _ in range(27)]
        return self._computeMinDistance(text, 26, 26, 0, dp)
    def _computeMinDistance(self, text: str, leftPos: int, rightPos: int, index: int, dp: list[list[list[int]]]) -> int:
        if index == len(text):
            return 0
        if dp[leftPos][rightPos][index] is not None:
            return dp[leftPos][rightPos][index]
        targetChar = ord(text[index]) - ord('A')
        moveLeft = self._calculateManhattanDistance(leftPos, targetChar) + self._computeMinDistance(text, targetChar, rightPos, index + 1, dp)
        moveRight = self._calculateManhattanDistance(rightPos, targetChar) + self._computeMinDistance(text, leftPos, targetChar, index + 1, dp)
        dp[leftPos][rightPos][index] = min(moveLeft, moveRight)
        return dp[leftPos][rightPos][index]
    def _calculateManhattanDistance(self, pos1: int, pos2: int) -> int:
        if pos1 == 26:
            return 0
        x1 = pos1 // 6
        y1 = pos1 % 6
        x2 = pos2 // 6
        y2 = pos2 % 6
        distX = x1 - x2
        distY = y1 - y2
        return (distX if distX >= 0 else -distX) + (distY if distY >= 0 else -distY)

