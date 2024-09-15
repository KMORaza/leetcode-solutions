from collections import deque
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = deque()
        for c in expression:
            if c not in '(),':
                stack.append(c)
            elif c == ')':
                count_true = 0
                count_false = 0
                while stack and stack[-1] in 'tf':
                    if stack[-1] == 't':
                        count_true += 1
                    else:
                        count_false += 1
                    stack.pop()
                operator = stack.pop()
                if operator == '!' and count_false > 0:
                    result = 't'
                elif operator == '&' and count_false == 0:
                    result = 't'
                elif operator == '|' and count_true > 0:
                    result = 't'
                else:
                    result = 'f'
                stack.append(result)
        return stack[-1] == 't'
