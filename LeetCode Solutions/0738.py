class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))
        length = len(digits)
        mark = -1
        for i in range(length - 1):
            if digits[i] > digits[i + 1]:
                mark = i
                break
        if mark == -1:
            return n
        while mark > 0 and digits[mark] == digits[mark - 1]:
            mark -= 1
        digits[mark] -= 1
        for i in range(mark + 1, length):
            digits[i] = 9
        return int(''.join(map(str, digits)))
