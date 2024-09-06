class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int, path: list[int]):
            if len(path) >= 2:
                result.add(tuple(path))
            used = set()
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    if nums[i] not in used:
                        used.add(nums[i])
                        backtrack(i + 1, path + [nums[i]])
        result = set()
        backtrack(0, [])
        return [list(seq) for seq in result]
