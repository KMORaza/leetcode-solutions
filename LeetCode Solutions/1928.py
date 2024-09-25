import heapq
from collections import defaultdict
from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        city_count = len(passingFees)
        road_map = defaultdict(list)
        for start_city, end_city, travel_duration in edges:
            road_map[start_city].append((end_city, travel_duration))
            road_map[end_city].append((start_city, travel_duration))
        return self._find_minimum_cost(road_map, 0, city_count - 1, maxTime, passingFees)
    def _find_minimum_cost(self, road_map: defaultdict, source: int, destination: int, maxTime: int, fees: List[int]) -> int:
        total_cost = [float('inf')] * len(road_map)
        total_time = [maxTime + 1] * len(road_map)
        priority_queue = []
        total_cost[source] = fees[source]
        total_time[source] = 0
        heapq.heappush(priority_queue, (total_cost[source], total_time[source], source))
        while priority_queue:
            current_cost, current_time, current_location = heapq.heappop(priority_queue)
            if current_location == destination:
                return total_cost[destination]
            if current_time > total_time[current_location] and current_cost > total_cost[current_location]:
                continue
            for neighbor, travel_duration in road_map[current_location]:
                if current_time + travel_duration > maxTime:
                    continue
                if current_cost + fees[neighbor] < total_cost[neighbor]:
                    total_cost[neighbor] = current_cost + fees[neighbor]
                    total_time[neighbor] = current_time + travel_duration
                    heapq.heappush(priority_queue, (total_cost[neighbor], total_time[neighbor], neighbor))
                elif current_time + travel_duration < total_time[neighbor]:
                    total_time[neighbor] = current_time + travel_duration
                    heapq.heappush(priority_queue, (current_cost + fees[neighbor], total_time[neighbor], neighbor))
        return -1
