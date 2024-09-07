from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        expected_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
        actual_sum = 0
        actual_sum_of_squares = 0
        for num in nums:
            actual_sum += num
            actual_sum_of_squares += num * num
        sum_diff = expected_sum - actual_sum
        sum_of_squares_diff = expected_sum_of_squares - actual_sum_of_squares
        sum_missing_plus_duplicate = sum_of_squares_diff // sum_diff
        missing_number = (sum_diff + sum_missing_plus_duplicate) // 2
        duplicate_number = missing_number - sum_diff
        return [duplicate_number, missing_number]
