from itertools import permutations, product
class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def calculate(a, b, op):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/':
                if b == 0: return float('inf')
                return a / b
        def backtrack(numbers):
            if len(numbers) == 1:
                return abs(numbers[0] - 24) < 1e-6
            for i in range(len(numbers)):
                for j in range(len(numbers)):
                    if i != j:
                        new_numbers = [numbers[k] for k in range(len(numbers)) if k != i and k != j]
                        for op in '+-*/':
                            if op in '+-*/':
                                result = calculate(numbers[i], numbers[j], op)
                                new_numbers.append(result)
                                if backtrack(new_numbers):
                                    return True
                                new_numbers.pop()
            return False
        for perm in permutations(cards):
            if backtrack(list(perm)):
                return True
        return False
