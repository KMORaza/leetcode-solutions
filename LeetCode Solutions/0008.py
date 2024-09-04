class Solution:
    def myAtoi(self, s):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        index, sign, total = 0, 1, 0
        n = len(s)
        while index < n and s[index] == ' ':
            index += 1
        if index < n and s[index] in ['+', '-']:
            sign = -1 if s[index] == '-' else 1
            index += 1
        while index < n and s[index].isdigit():
            digit = int(s[index])
            if total > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            total = total * 10 + digit
            index += 1
        return sign * total