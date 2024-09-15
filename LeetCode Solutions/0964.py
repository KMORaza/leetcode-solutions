class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        self.memoization = {}
        return self.dfs(x, target)
    def dfs(self, x: int, target: int) -> int:
        if target in self.memoization:
            return self.memoization[target]
        if x > target:
            result = min(2 * target - 1, 2 * (x - target))
            self.memoization[target] = result
            return result
        if x == target:
            self.memoization[target] = 0
            return 0
        prod = x
        n = 0
        while prod < target:
            prod *= x
            n += 1
        if prod == target:
            self.memoization[target] = n
            return n
        output = self.dfs(x, target - prod // x) + n
        if prod < 2 * target:
            output = min(output, self.dfs(x, prod - target) + n + 1)
        self.memoization[target] = output
        return output
