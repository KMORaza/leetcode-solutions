import heapq
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            if val > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
