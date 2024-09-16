from typing import List
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = []
        cost = 0
        for value in arr:
            while stack and stack[-1] <= value:
                mid = stack.pop()
                if stack:
                    cost += mid * min(stack[-1], value)
                else:
                    cost += mid * value
            stack.append(value)
        while len(stack) > 1:
            cost += stack.pop() * stack[-1]
        return cost
