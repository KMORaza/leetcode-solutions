from collections import deque
class Solution:
    def minNumberOfSemesters(self, numCourses: int, prerequisites: list[list[int]], maxCoursesPerSemester: int) -> int:
        prereq_mask = [0] * numCourses
        for pre, course in prerequisites:
            prereq_mask[course - 1] |= 1 << (pre - 1)
        min_semesters = [float('inf')] * (1 << numCourses)
        min_semesters[0] = 0
        queue = deque([0])
        while queue:
            current_mask = queue.popleft()
            available_courses_mask = 0
            for course_index in range(numCourses):
                if (current_mask & prereq_mask[course_index]) == prereq_mask[course_index]:
                    available_courses_mask |= 1 << course_index
            available_courses_mask &= ~current_mask
            subset = available_courses_mask
            while subset > 0:
                if bin(subset).count('1') <= maxCoursesPerSemester:
                    new_mask = current_mask | subset
                    if min_semesters[new_mask] > min_semesters[current_mask] + 1:
                        min_semesters[new_mask] = min_semesters[current_mask] + 1
                        queue.append(new_mask)
                subset = (subset - 1) & available_courses_mask
        return min_semesters[(1 << numCourses) - 1]
