from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True, key=lambda x: x[0])
        fleets = 0
        prev_time = 0
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            if time_to_target > prev_time:
                fleets += 1
                prev_time = time_to_target
        return fleets
