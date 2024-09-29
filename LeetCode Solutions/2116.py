class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        balance = 0
        free = 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    balance += 1
                else:
                    balance -= 1
            else:
                free += 1
            if balance < 0:
                if free > 0:
                    free -= 1
                    balance += 1
                else:
                    return False
        balance = 0
        free = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    balance += 1
                else:
                    balance -= 1
            else:
                free += 1
            if balance < 0:
                if free > 0:
                    free -= 1
                    balance += 1
                else:
                    return False
        return True