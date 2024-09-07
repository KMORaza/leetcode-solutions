class Solution:
    def checkValidString(self, s: str) -> bool:
        def valid_pass(s: str, open_bracket: str, close_bracket: str) -> bool:
            balance = 0
            for char in s:
                if char == open_bracket or char == '*':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return True
        if not valid_pass(s, '(', ')'):
            return False
        if not valid_pass(s[::-1], ')', '('):
            return False
        return True
