class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        last_pos = [-1] * 32  # Track last position where each bit is set

        for i in range(n - 1, -1, -1):
            max_or = nums[i]
            farthest = i

            for bit in range(32):
                if nums[i] & (1 << bit):
                    last_pos[bit] = i

                if last_pos[bit] != -1:
                    farthest = max(farthest, last_pos[bit])

            result[i] = farthest - i + 1

        return result