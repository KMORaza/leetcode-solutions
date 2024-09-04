class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k > n
        temp = [0] * n
        for i in range(n):
            temp[(i + k) % n] = nums[i]
        nums[:] = temp
