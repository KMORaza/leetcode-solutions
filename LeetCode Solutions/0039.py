class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])
        result = []
        backtrack(0, target, [])
        return result