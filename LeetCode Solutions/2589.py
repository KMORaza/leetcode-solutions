class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])

        running = [False] * 2001

        for start, end, duration in tasks:
            curr_duration = 0
            for t in range(start, end + 1):
                if running[t]:
                    curr_duration += 1

            needed = duration - curr_duration
            t = end
            while needed > 0 and t >= start:
                if not running[t]:
                    running[t] = True
                    needed -= 1
                t -= 1

        return sum(running)