class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq

        meetings.sort()
        free_rooms = list(range(n))
        busy_rooms = []
        room_count = [0] * n

        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room_idx = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room_idx)

            if free_rooms:
                room_idx = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room_idx))
                room_count[room_idx] += 1
            else:
                release_time, room_idx = heapq.heappop(busy_rooms)
                new_end = release_time + (end - start)
                heapq.heappush(busy_rooms, (new_end, room_idx))
                room_count[room_idx] += 1

        max_bookings = max(room_count)
        for i in range(n):
            if room_count[i] == max_bookings:
                return i