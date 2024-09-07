import heapq
class Solution:
    def scheduleCourse(self, courses):
        courses.sort(key=lambda x: x[1])
        max_heap = []
        total_time = 0
        for duration, last_day in courses:
            heapq.heappush(max_heap, -duration)
            total_time += duration
            if total_time > last_day:
                total_time += heapq.heappop(max_heap)
        return len(max_heap)
