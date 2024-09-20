import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        for pass_students, total_students in classes:
            heapq.heappush(max_heap, (-((pass_students + 1) / (total_students + 1) - pass_students / total_students), pass_students, total_students))
        for _ in range(extraStudents):
            _, pass_students, total_students = heapq.heappop(max_heap)
            pass_students += 1
            total_students += 1
            heapq.heappush(max_heap, (-((pass_students + 1) / (total_students + 1) - pass_students / total_students), pass_students, total_students))
        total_average = sum(pass_students / total_students for _, pass_students, total_students in max_heap)
        return total_average / len(classes)