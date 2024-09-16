class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def compute_moves_for_pattern(nums, pattern_type):
            moves = 0
            n = len(nums)
            for i in range(n):
                left = nums[i - 1] if i - 1 >= 0 else float('inf')
                right = nums[i + 1] if i + 1 < n else float('inf')
                if pattern_type == 'even':
                    if i % 2 == 0:
                        if nums[i] >= min(left, right):
                            moves += nums[i] - min(left, right) + 1
                elif pattern_type == 'odd':
                    if i % 2 != 0:
                        if nums[i] >= min(left, right):
                            moves += nums[i] - min(left, right) + 1
            return moves
        moves_for_even_pattern = compute_moves_for_pattern(nums, 'even')
        moves_for_odd_pattern = compute_moves_for_pattern(nums, 'odd')
        return min(moves_for_even_pattern, moves_for_odd_pattern)
