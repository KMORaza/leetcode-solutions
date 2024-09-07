class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_length = 0
        def compute_length(start):
            length = 0
            current = start
            while not visited[current]:
                visited[current] = True
                current = nums[current]
                length += 1
            return length
        for i in range(n):
            if not visited[i]:
                max_length = max(max_length, compute_length(i))
        return max_length
