class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        total_distance = sum(distance)
        clockwise_distance = sum(distance[start:destination])
        counter_clockwise_distance = total_distance - clockwise_distance
        return min(clockwise_distance, counter_clockwise_distance)
