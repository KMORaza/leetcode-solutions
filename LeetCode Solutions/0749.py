from typing import List, Set, Dict
class Region:
    def __init__(self):
        self.infected: Set[int] = set()
        self.noninfected: Set[int] = set()
        self.wallsRequired: int = 0
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m = len(isInfected)
        n = len(isInfected[0])
        ans = 0
        while True:
            regions = []
            seen = [[False] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not seen[i][j]:
                        region = Region()
                        self.dfs(isInfected, i, j, region, seen)
                        if region.noninfected:
                            regions.append(region)
            if not regions:
                break
            regions.sort(key=lambda r: len(r.noninfected))
            mostInfectedRegion = regions.pop()
            ans += mostInfectedRegion.wallsRequired
            for neighbor in mostInfectedRegion.infected:
                i, j = divmod(neighbor, n)
                isInfected[i][j] = 2
            for region in regions:
                for neighbor in region.noninfected:
                    i, j = divmod(neighbor, n)
                    isInfected[i][j] = 1
        return ans
    def dfs(self, isInfected: List[List[int]], i: int, j: int, region: Region, seen: List[List[bool]]):
        if i < 0 or i >= len(isInfected) or j < 0 or j >= len(isInfected[0]):
            return
        if seen[i][j] or isInfected[i][j] == 2:
            return
        if isInfected[i][j] == 0:
            region.noninfected.add(i * len(isInfected[0]) + j)
            region.wallsRequired += 1
            return
        seen[i][j] = True
        region.infected.add(i * len(isInfected[0]) + j)
        self.dfs(isInfected, i + 1, j, region, seen)
        self.dfs(isInfected, i - 1, j, region, seen)
        self.dfs(isInfected, i, j + 1, region, seen)
        self.dfs(isInfected, i, j - 1, region, seen)
