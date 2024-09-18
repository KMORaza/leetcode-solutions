from typing import List
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = 0
        slowest_key = ''
        previous_time = 0
        for i in range(len(releaseTimes)):
            current_duration = releaseTimes[i] - previous_time
            previous_time = releaseTimes[i]
            if (current_duration > max_duration) or (current_duration == max_duration and keysPressed[i] > slowest_key):
                max_duration = current_duration
                slowest_key = keysPressed[i]
        return slowest_key
