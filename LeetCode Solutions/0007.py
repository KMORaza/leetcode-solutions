class Solution:
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x *= sign
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if (reversed_x > (INT_MAX - digit) // 10):
                return 0
            reversed_x = reversed_x * 10 + digit
        reversed_x *= sign
        return reversed_x