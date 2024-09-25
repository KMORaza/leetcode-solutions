from typing import List
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def compatibility(student, mentor):
            return sum(s == m for s, m in zip(student, mentor))
        n = len(students)
        max_score = 0
        def backtrack(used, current_score):
            nonlocal max_score
            if len(used) == n:
                max_score = max(max_score, current_score)
                return
            for i in range(n):
                if i not in used:
                    used.add(i)
                    backtrack(used, current_score + compatibility(students[len(used)-1], mentors[i]))
                    used.remove(i)
        backtrack(set(), 0)
        return max_score