class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == 'a':
                stack.append('a')
            elif char == 'b':
                if not stack or stack[-1] != 'a':
                    return False
                stack.pop()
                stack.append('b')
            elif char == 'c':
                if not stack or stack[-1] != 'b':
                    return False
                stack.pop()
            else:
                return False
        return not stack