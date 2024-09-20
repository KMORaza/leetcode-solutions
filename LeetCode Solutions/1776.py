from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        result = [float('inf')] * n
        stack = []
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]
            while stack:
                j = stack[-1]
                if speed <= cars[j][1]:
                    stack.pop()
                    continue
                time = (cars[j][0] - position) / (speed - cars[j][1])
                if time > result[j]:
                    stack.pop()
                    continue
                result[i] = time
                break
            stack.append(i)
        for i in range(n):
            if result[i] == float('inf'):
                result[i] = -1.0
        return result
