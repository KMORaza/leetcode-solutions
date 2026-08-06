class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        powers = []
        power = 0
        temp_n = n
        while temp_n:
            if temp_n & 1:
                powers.append(power)
            temp_n >>= 1
            power += 1

        result = []
        for left, right in queries:
            product = 1
            for i in range(left, right + 1):
                product = (product * (2 ** powers[i])) % MOD
            result.append(product)

        return result