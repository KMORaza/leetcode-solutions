class Solution:
    def __init__(self):
        self.cache = None
        self.maxAllowedRolls = None
    def dieSimulator(self, n: int, maxAllowedRolls: list[int]) -> int:
        self.cache = [[[None for _ in range(16)] for _ in range(7)] for _ in range(n)]
        self.maxAllowedRolls = maxAllowedRolls
        return self.dfs(0, 0, 0)
    def dfs(self, currentRolls: int, previousFace: int, consecutiveRolls: int) -> int:
        if currentRolls >= len(self.cache):
            return 1
        if self.cache[currentRolls][previousFace][consecutiveRolls] is not None:
            return self.cache[currentRolls][previousFace][consecutiveRolls]
        totalSequences = 0
        for newFace in range(1, 7):
            if newFace != previousFace:
                totalSequences += self.dfs(currentRolls + 1, newFace, 1)
            elif consecutiveRolls < self.maxAllowedRolls[previousFace - 1]:
                totalSequences += self.dfs(currentRolls + 1, previousFace, consecutiveRolls + 1)
        totalSequences %= 1000000007
        self.cache[currentRolls][previousFace][consecutiveRolls] = totalSequences
        return totalSequences