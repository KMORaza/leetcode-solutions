class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total_distance = 0
        for i in range(32):
            count_of_ones = sum((num >> i) & 1 for num in nums)
            count_of_zeros = n - count_of_ones
            total_distance += count_of_ones * count_of_zeros
        return total_distance
