class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while not self.checkBalance(n):
            n += 1
        return n
    def checkBalance(self, value: int) -> bool:
        digit_count = [0] * 10
        while value > 0:
            current_digit = value % 10
            if current_digit == 0:
                return False
            digit_count[current_digit] += 1
            value //= 10
        for i in range(1, 10):
            if digit_count[i] > 0 and digit_count[i] != i:
                return False
        return True
