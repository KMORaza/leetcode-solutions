from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        left_smaller = [0] * n
        right_larger = [0] * n
        left_larger = [0] * n
        right_smaller = [0] * n
        for i in range(n):
            for j in range(i):
                if rating[j] < rating[i]:
                    left_smaller[i] += 1
                if rating[j] > rating[i]:
                    left_larger[i] += 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    right_larger[i] += 1
                if rating[j] < rating[i]:
                    right_smaller[i] += 1
        result = 0
        for i in range(n):
            result += left_smaller[i] * right_larger[i]
            result += left_larger[i] * right_smaller[i]
        return result
