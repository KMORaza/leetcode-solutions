from typing import List
import operator
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], op: str) -> List[int]:
            ops = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul
            }
            return [ops[op](l, r) for l in left for r in right]
        def ways(expr: str) -> List[int]:
            if expr.isdigit():
                return [int(expr)]
            if expr in memo:
                return memo[expr]
            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left = ways(expr[:i])
                    right = ways(expr[i + 1:])
                    results.extend(compute(left, right, char))
            memo[expr] = results
            return results
        memo = {}
        return ways(expression)
