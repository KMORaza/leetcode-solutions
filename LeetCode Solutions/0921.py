class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        close_needed = 0
        for char in s:
            if char == '(':
                open_needed += 1
            elif char == ')':
                if open_needed > 0:
                    open_needed -= 1
                else:
                    close_needed += 1
        return open_needed + close_needed
