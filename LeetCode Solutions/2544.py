class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.reverse()
        result = 0
        for i in range(len(digits)):
            if i % 2 == 0:
                result += digits[i]
            else:
                result -= digits[i]

        return result