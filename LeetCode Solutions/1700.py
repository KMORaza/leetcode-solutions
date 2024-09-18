from collections import Counter
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = Counter(students)
        for sandwich in sandwiches:
            if student_count[sandwich] == 0:
                break
            student_count[sandwich] -= 1
        return sum(student_count.values())
