class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(m):
            for j in range(n):
                product = int(num1[i]) * int(num2[j])
                sum_ = product + result[i + j]
                result[i + j] = sum_ % 10
                result[i + j + 1] += sum_ // 10
        while result[-1] == 0:
            result.pop()
        return ''.join(map(str, result[::-1]))
