from math import factorial
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        def permutations(n, k):
            return factorial(n) // factorial(n - k)
        count = 1
        for i in range(1, n + 1):
            if i > 10:
                break
            count += 9 * permutations(9, i - 1)
        return count