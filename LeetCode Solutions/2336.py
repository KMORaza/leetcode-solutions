import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.min_heap = []
        self.added_back = set()
        self.current_min = 1

    def popSmallest(self):
        if self.min_heap and self.min_heap[0] < self.current_min:
            smallest = heapq.heappop(self.min_heap)
            self.added_back.remove(smallest)
            return smallest
        else:
            smallest = self.current_min
            self.current_min += 1
            return smallest

    def addBack(self, num):
        if num < self.current_min and num not in self.added_back:
            heapq.heappush(self.min_heap, num)
            self.added_back.add(num)