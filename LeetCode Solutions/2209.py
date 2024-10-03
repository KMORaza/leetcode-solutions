class Solution:
    x = 1000
    def minimumWhiteTiles(self, layout: str, carpetQty: int, lengthOfCarpet: int) -> int:
        memoization = [[self.x] * (carpetQty + 1) for _ in range(len(layout) + 1)]
        return self._calculateTiles(layout, 0, carpetQty, lengthOfCarpet, memoization)
    def _calculateTiles(self, layout: str, position: int, remainingCarpets: int, lengthOfCarpet: int, memoization: list) -> int:
        if remainingCarpets < 0:
            return self.x
        if position >= len(layout):
            return 0
        if memoization[position][remainingCarpets] != self.x:
            return memoization[position][remainingCarpets]
        placeCarpet = self._calculateTiles(layout, position + lengthOfCarpet, remainingCarpets - 1, lengthOfCarpet, memoization)
        leaveTile = self._calculateTiles(layout, position + 1, remainingCarpets, lengthOfCarpet, memoization) + int(layout[position])
        memoization[position][remainingCarpets] = min(placeCarpet, leaveTile)
        return memoization[position][remainingCarpets]
