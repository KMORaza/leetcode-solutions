class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False] * n
        indexed_nums = [(nums[i], i) for i in range(n)]
        indexed_nums.sort()

        score = 0

        for val, idx in indexed_nums:
            if not marked[idx]:
                score += val
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True

        return score