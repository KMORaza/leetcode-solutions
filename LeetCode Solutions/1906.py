from typing import List
class Solution:
    def minDifference(self, input_array: List[int], query_array: List[List[int]]) -> List[int]:
        output = []
        num_positions = [[] for _ in range(101)]
        for index, num in enumerate(input_array):
            num_positions[num].append(index)
        for start_idx, end_idx in query_array:
            min_diff = float('inf')
            last_num = -1
            for num in range(1, 101):
                if not num_positions[num]:
                    continue
                positions = num_positions[num]
                left = self.find_first_greater_equal(positions, start_idx)
                if left < len(positions) and positions[left] <= end_idx:
                    if last_num != -1:
                        min_diff = min(min_diff, num - last_num)
                    last_num = num
            output.append(min_diff if min_diff != float('inf') else -1)
        return output
    def find_first_greater_equal(self, positions: List[int], target: int) -> int:
        low, high = 0, len(positions)
        while low < high:
            mid = (low + high) // 2
            if positions[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
