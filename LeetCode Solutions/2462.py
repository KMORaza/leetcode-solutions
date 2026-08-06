import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        total_cost = 0

        if 2 * candidates >= n:
            costs.sort()
            return sum(costs[:k])

        left_heap = []
        right_heap = []

        for i in range(candidates):
            heapq.heappush(left_heap, (costs[i], i))

        for i in range(n - candidates, n):
            heapq.heappush(right_heap, (costs[i], i))

        left_idx = candidates
        right_idx = n - candidates - 1

        for _ in range(k):
            left_min = left_heap[0] if left_heap else (float('inf'), -1)
            right_min = right_heap[0] if right_heap else (float('inf'), -1)

            if left_min[0] < right_min[0] or (left_min[0] == right_min[0] and left_min[1] < right_min[1]):
                total_cost += left_min[0]
                heapq.heappop(left_heap)

                if left_idx <= right_idx:
                    heapq.heappush(left_heap, (costs[left_idx], left_idx))
                    left_idx += 1
            else:
                total_cost += right_min[0]
                heapq.heappop(right_heap)

                if right_idx >= left_idx:
                    heapq.heappush(right_heap, (costs[right_idx], right_idx))
                    right_idx -= 1

        return total_cost