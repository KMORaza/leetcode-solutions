from typing import List
import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for index, (arrival, departure) in enumerate(times):
            events.append((arrival, index, 'arrive'))
            events.append((departure, index, 'depart'))
        events.sort(key=lambda x: (x[0], x[2] == 'arrive'))
        available_chairs = []
        for chair in range(len(times)):
            heapq.heappush(available_chairs, chair)
        chair_assignment = {}
        for event in events:
            time, friend_index, event_type = event
            if event_type == 'arrive':
                chair = heapq.heappop(available_chairs)
                chair_assignment[friend_index] = chair
                if friend_index == targetFriend:
                    return chair
            else:
                chair = chair_assignment[friend_index]
                heapq.heappush(available_chairs, chair)
        return -1
