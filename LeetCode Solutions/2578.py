class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10

        digits.sort()

        num1_str = ""
        num2_str = ""

        for i in range(len(digits)):
            if i % 2 == 0:
                num1_str += str(digits[i])
            else:
                num2_str += str(digits[i])

        num1 = int(num1_str) if num1_str else 0
        num2 = int(num2_str) if num2_str else 0

        return num1 + num2