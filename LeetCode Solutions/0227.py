class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_num = 0
        operation = '+'
        s = s.replace(" ", "")
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            if char in '+-*/' or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack.append(stack.pop() * current_num)
                elif operation == '/':
                    top = stack.pop()
                    stack.append(int(top / current_num))
                operation = char
                current_num = 0
        return sum(stack)
