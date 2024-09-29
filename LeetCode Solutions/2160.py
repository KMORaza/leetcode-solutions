class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(str(num))
        num1 = int(digits[0] + digits[2])
        num2 = int(digits[1] + digits[3])
        return num1 + num2
