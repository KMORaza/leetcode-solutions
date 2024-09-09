import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def fraction_value(numerator, denominator):
            return numerator / denominator
        n = len(arr)
        min_heap = []
        for j in range(1, n):
            heapq.heappush(min_heap, (fraction_value(arr[0], arr[j]), arr[0], arr[j], 0, j))
        for _ in range(k):
            _, numerator, denominator, i, j = heapq.heappop(min_heap)
            if i + 1 < j:
                heapq.heappush(min_heap, (fraction_value(arr[i + 1], arr[j]), arr[i + 1], arr[j], i + 1, j))
        return [numerator, denominator]
