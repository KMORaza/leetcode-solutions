import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        min_heap = []
        max_heap = []
        for i in range(len(profits)):
            heapq.heappush(min_heap, (capital[i], profits[i]))
        current_capital = w
        for _ in range(k):
            while min_heap and min_heap[0][0] <= current_capital:
                cap, prof = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -prof)
            if not max_heap:
                break
            max_profit = -heapq.heappop(max_heap)
            current_capital += max_profit
        return current_capital
