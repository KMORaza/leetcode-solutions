class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        def backtrack(start, k, n, path):
            if k == 0 and n == 0:
                result.append(path)
                return
            if k == 0 or n < 0:
                return
            for i in range(start, 10):
                backtrack(i + 1, k - 1, n - i, path + [i])
        result = []
        backtrack(1, k, n, [])
        return result