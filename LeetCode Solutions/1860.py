from typing import List
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        time = 0
        while True:
            time += 1
            if memory1 >= memory2 and memory1 >= time:
                memory1 -= time
            elif memory2 >= memory1 and memory2 >= time:
                memory2 -= time
            else:
                break
        return [time, memory1, memory2]