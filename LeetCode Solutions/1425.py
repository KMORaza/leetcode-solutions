from collections import deque
class Solution:
    def constrainedSubsetSum(self, array: list[int], window_size: int) -> int:
        length = len(array)
        max_sums = [0] * length
        max_result = float('-inf')
        indices_deque = deque()
        for idx in range(length):
            if indices_deque and idx - indices_deque[0] > window_size:
                indices_deque.popleft()
            max_sums[idx] = max(0, max_sums[indices_deque[0]] if indices_deque else 0) + array[idx]
            while indices_deque and max_sums[indices_deque[-1]] <= max_sums[idx]:
                indices_deque.pop()
            indices_deque.append(idx)
            max_result = max(max_result, max_sums[idx])
        return max_result
