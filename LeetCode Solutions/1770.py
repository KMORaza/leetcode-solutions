class Solution:
    def maximumScore(self, array: List[int], factors: List[int]) -> int:
        cache = [[None] * len(factors) for _ in range(len(factors))]
        return self.calculateScore(array, 0, factors, 0, cache)
    def calculateScore(self, array: List[int], start: int, factors: List[int], index: int, cache: List[List[Optional[int]]]) -> int:
        if index == len(factors):
            return 0
        if cache[start][index] is not None:
            return cache[start][index]
        end = len(array) - (index - start) - 1
        pick_from_start = array[start] * factors[index] + self.calculateScore(array, start + 1, factors, index + 1, cache)
        pick_from_end = array[end] * factors[index] + self.calculateScore(array, start, factors, index + 1, cache)
        cache[start][index] = max(pick_from_start, pick_from_end)
        return cache[start][index]
