class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_negative = num < 0
        num = abs(num)
        base7_digits = []
        while num > 0:
            remainder = num % 7
            base7_digits.append(str(remainder))
            num //= 7
        if is_negative:
            base7_digits.append('-')
        return ''.join(reversed(base7_digits))
