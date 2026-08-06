import heapq


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        workers = []
        for i in range(k):
            efficiency = time[i][0] + time[i][2]
            heapq.heappush(workers, (-efficiency, -i))

        left_waiting = []
        right_waiting = []

        left_finish = []
        right_finish = []

        t = 0
        boxes_moved = 0

        for i in range(k):
            heapq.heappush(left_waiting, heapq.heappop(workers))

        while boxes_moved < n:
            while left_finish and left_finish[0][0] <= t:
                _, eff, idx = heapq.heappop(left_finish)
                heapq.heappush(left_waiting, (eff, idx))

            while right_finish and right_finish[0][0] <= t:
                _, eff, idx = heapq.heappop(right_finish)
                heapq.heappush(right_waiting, (eff, idx))

            if right_waiting:
                eff, idx = heapq.heappop(right_waiting)
                worker_idx = -idx
                t += time[worker_idx][2]
                put_time = t + time[worker_idx][3]
                heapq.heappush(left_finish, (put_time, eff, idx))
                boxes_moved += 1
            elif left_waiting and n - boxes_moved > len(right_finish) + len(right_waiting):
                eff, idx = heapq.heappop(left_waiting)
                worker_idx = -idx
                t += time[worker_idx][0]
                pick_time = t + time[worker_idx][1]
                heapq.heappush(right_finish, (pick_time, eff, idx))
            else:
                next_time = float('inf')
                if left_finish and n - boxes_moved > len(right_finish) + len(right_waiting):
                    next_time = min(next_time, left_finish[0][0])
                if right_finish:
                    next_time = min(next_time, right_finish[0][0])

                if next_time != float('inf'):
                    t = next_time

        return t