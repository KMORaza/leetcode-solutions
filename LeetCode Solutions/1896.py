class Solution:
    def minOperationsToFlip(self, input_expr: str) -> int:
        from collections import deque
        state_stack = deque()
        toggle_pair = None
        for symbol in input_expr:
            if symbol in '(&|':
                state_stack.append((symbol, 0))
                continue
            if symbol == ')':
                toggle_pair = state_stack.pop()
                state_stack.pop()
            else:
                toggle_pair = (symbol, 1)
            if state_stack and state_stack[-1][0] in '&|':
                operation = state_stack.pop()[0]
                first_symbol = state_stack[-1][0]
                first_cost = state_stack.pop()[1]
                second_symbol = toggle_pair[0]
                second_cost = toggle_pair[1]
                if operation == '&':
                    if first_symbol == '0' and second_symbol == '0':
                        toggle_pair = ('0', 1 + min(first_cost, second_cost))
                    elif first_symbol == '0' and second_symbol == '1':
                        toggle_pair = ('0', 1)
                    elif first_symbol == '1' and second_symbol == '0':
                        toggle_pair = ('0', 1)
                    else:
                        toggle_pair = ('1', min(first_cost, second_cost))
                else:
                    if first_symbol == '0' and second_symbol == '0':
                        toggle_pair = ('0', min(first_cost, second_cost))
                    elif first_symbol == '0' and second_symbol == '1':
                        toggle_pair = ('1', 1)
                    elif first_symbol == '1' and second_symbol == '0':
                        toggle_pair = ('1', 1)
                    else:
                        toggle_pair = ('1', 1 + min(first_cost, second_cost))
            state_stack.append(toggle_pair)
        return state_stack[-1][1]
