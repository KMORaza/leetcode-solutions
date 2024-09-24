import math
from typing import List
class Solution:
    def minSkips(self, travel_distances: List[int], vehicle_velocity: int, time_limit: int) -> int:
        MAX_VALUE = 10000000.0
        SMALL_MARGIN = 0.000000001
        total_segments = len(travel_distances)
        time_table = [[MAX_VALUE] * (total_segments + 1) for _ in range(total_segments + 1)]
        time_table[0][0] = 0
        for segment_index in range(1, total_segments + 1):
            distance_current = travel_distances[segment_index - 1]
            time_table[segment_index][0] = math.ceil(time_table[segment_index - 1][0] + distance_current / vehicle_velocity - SMALL_MARGIN)
            for skip_count in range(1, segment_index + 1):
                time_table[segment_index][skip_count] = min(
                    time_table[segment_index - 1][skip_count - 1] + distance_current / vehicle_velocity,
                    math.ceil(time_table[segment_index - 1][skip_count] + distance_current / vehicle_velocity - SMALL_MARGIN)
                )
        for skip_count in range(total_segments + 1):
            if time_table[total_segments][skip_count] <= time_limit:
                return skip_count
        return -1