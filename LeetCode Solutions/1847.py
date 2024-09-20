from typing import List
import bisect
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        results = [-1] * len(queries)
        query_indices = list(range(len(queries)))
        rooms.sort(key=lambda x: x[1], reverse=True)
        query_indices.sort(key=lambda i: queries[i][1], reverse=True)
        available_room_ids = []
        room_index = 0
        for idx in query_indices:
            while room_index < len(rooms) and rooms[room_index][1] >= queries[idx][1]:
                available_room_ids.append(rooms[room_index][0])
                room_index += 1
            results[idx] = self.findClosestRoomId(available_room_ids, queries[idx][0])
        return results
    def findClosestRoomId(self, available_room_ids: List[int], preferred_id: int) -> int:
        if not available_room_ids:
            return -1
        available_room_ids.sort()
        pos = bisect.bisect_left(available_room_ids, preferred_id)
        candidates = []
        if pos < len(available_room_ids):
            candidates.append(available_room_ids[pos])
        if pos > 0:
            candidates.append(available_room_ids[pos - 1])
        return min(candidates, key=lambda room_id: (abs(preferred_id - room_id), room_id), default=-1)
