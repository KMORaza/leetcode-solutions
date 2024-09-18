class Solution:
    x=1000000007
    def numberOfSets(self, total: int, segments: int) -> int:
        cache = [[[None for _ in range(2)] for _ in range(segments + 1)] for _ in range(total)]
        return self._calculateWays(0, segments, False, total, cache)
    def _calculateWays(self, index: int, segments: int, isDrawing: bool, total: int, cache: list) -> int:
        if segments == 0:
            return 1
        if index == total:
            return 0
        if cache[index][segments][1 if isDrawing else 0] is not None:
            return cache[index][segments][1 if isDrawing else 0]
        if isDrawing:
            cache[index][segments][1 if isDrawing else 0] = (
                self._calculateWays(index + 1, segments, True, total, cache) +
                self._calculateWays(index, segments - 1, False, total, cache)
            ) % self.x
        else:
            cache[index][segments][1 if isDrawing else 0] = (
                self._calculateWays(index + 1, segments, False, total, cache) +
                self._calculateWays(index + 1, segments, True, total, cache)
            ) % self.x
        return cache[index][segments][1 if isDrawing else 0]
