import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        max_heap = []
        current_fuel = startFuel
        prev_position = 0
        stops = 0
        for position, fuel in stations:
            distance = position - prev_position
            while max_heap and current_fuel < distance:
                current_fuel -= heapq.heappop(max_heap)
                stops += 1
            if current_fuel < distance:
                return -1
            current_fuel -= distance
            prev_position = position
            heapq.heappush(max_heap, -fuel)
        return stops
