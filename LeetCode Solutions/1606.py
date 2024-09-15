import heapq
from sortedcontainers import SortedList
from typing import List
class Solution:
    def busiestServers(self, num_servers: int, arrival_times: List[int], job_durations: List[int]) -> List[int]:
        job_count = [0] * num_servers
        server_heap = []
        available = SortedList(range(num_servers))
        for idx in range(len(arrival_times)):
            while server_heap and server_heap[0][0] <= arrival_times[idx]:
                _, server_id = heapq.heappop(server_heap)
                available.add(server_id)
            next_server = self.getAvailableServer(available, idx, num_servers)
            if next_server == -1:
                continue
            finish_time = arrival_times[idx] + job_durations[idx]
            heapq.heappush(server_heap, (finish_time, next_server))
            available.remove(next_server)
            job_count[next_server] += 1
        max_jobs = max(job_count)
        return [i for i, count in enumerate(job_count) if count == max_jobs]
    def getAvailableServer(self, available: SortedList, current_index: int, num_servers: int) -> int:
        if not available:
            return -1
        target_index = current_index % num_servers
        pos = available.bisect_left(target_index)
        if pos < len(available):
            return available[pos]
        return available[0]
