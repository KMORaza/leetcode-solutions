from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s: str) -> bool:
            balance = 0
            for char in s:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        queue = deque([s])
        visited = set([s])
        valid_strings = []
        found = False
        while queue:
            current = queue.popleft()
            if is_valid(current):
                valid_strings.append(current)
                found = True
            if found:
                continue
            for i in range(len(current)):
                if current[i] in ('(', ')'):
                    next_str = current[:i] + current[i+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
        return valid_strings
