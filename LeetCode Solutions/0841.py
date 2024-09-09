from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = set()
        queue = deque([0])
        while queue:
            room = queue.popleft()
            if room in visited:
                continue
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
        return len(visited) == n