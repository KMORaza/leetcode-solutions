class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors <= 3:
            return primeFactors
        x = 10**9 + 7
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, x)
        elif primeFactors % 3 == 1:
            return (pow(3, primeFactors // 3 - 1, x) * 4) % x
        else:
            return (pow(3, primeFactors // 3, x) * 2) % x
