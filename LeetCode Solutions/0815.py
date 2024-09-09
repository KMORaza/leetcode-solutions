from collections import deque, defaultdict
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(set)
        for bus_index, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].add(bus_index)
        queue = deque([source])
        visited_stops = set([source])
        visited_buses = set()
        buses_taken = 0
        while queue:
            for _ in range(len(queue)):
                current_stop = queue.popleft()
                for bus_index in stop_to_buses[current_stop]:
                    if bus_index in visited_buses:
                        continue
                    visited_buses.add(bus_index)
                    for stop in routes[bus_index]:
                        if stop == target:
                            return buses_taken + 1
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append(stop)
            buses_taken += 1
        return -1
