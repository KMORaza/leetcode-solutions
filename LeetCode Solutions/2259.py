class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        n = len(number)
        max_result = ""
        for i in range(n):
            if number[i] == digit:
                if i < n - 1 and number[i + 1] > digit:
                    candidate = number[:i] + number[i + 1:]
                    max_result = max(max_result, candidate)
                if i == n - 1 or (i < n - 1 and number[i + 1] <= digit):
                    candidate = number[:i] + number[i + 1:]
                    max_result = max(max_result, candidate)
        return max_result if max_result else ""
