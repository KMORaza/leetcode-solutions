from typing import List
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.max_log = 1
        while (1 << self.max_log) <= n:
            self.max_log += 1
        self.ancestor = [[-1] * self.max_log for _ in range(n)]
        for i in range(n):
            self.ancestor[i][0] = parent[i]
        for j in range(1, self.max_log):
            for i in range(n):
                if self.ancestor[i][j - 1] != -1:
                    self.ancestor[i][j] = self.ancestor[self.ancestor[i][j - 1]][j - 1]
    def getKthAncestor(self, node: int, k: int) -> int:
        current = node
        for j in range(self.max_log):
            if k & (1 << j):
                current = self.ancestor[current][j]
                if current == -1:
                    return -1
        return current
