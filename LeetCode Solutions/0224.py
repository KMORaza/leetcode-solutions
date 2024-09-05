class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        result = 0
        sign = 1
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '+':
                result += sign * current_number
                sign = 1
                current_number = 0
            elif char == '-':
                result += sign * current_number
                sign = -1
                current_number = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * current_number
                current_number = 0
                result *= stack.pop()
                result += stack.pop()
            elif char == ' ':
                continue
        result += sign * current_number
        return result
