class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def remove_invalid(s: str, open_paren: str, close_paren: str) -> str:
            result = []
            balance = 0
            for char in s:
                if char == open_paren:
                    balance += 1
                elif char == close_paren:
                    if balance == 0:
                        continue
                    balance -= 1
                result.append(char)
            return ''.join(result)
        s = remove_invalid(s, '(', ')')
        s = remove_invalid(s[::-1], ')', '(')
        return s[::-1]