x = 1000000007
class Solution:
    def __init__(self):
        self.factorial_cache = {0: 1}
        self.inv_factorial_cache = {0: 1}
        self.prime_factor_map = {}
    def mod_inverse(self, base, mod):
        outcome = 1
        exponent = mod - 2
        while exponent > 0:
            if exponent % 2 == 1:
                outcome = outcome * base % mod
            base = base * base % mod
            exponent //= 2
        return outcome
    def compute_factorial_and_inverse(self, limit):
        if limit in self.factorial_cache:
            return
        max_computed = max(self.factorial_cache.keys())
        for i in range(max_computed + 1, limit + 1):
            self.factorial_cache[i] = self.factorial_cache[i - 1] * i % x
            self.inv_factorial_cache[i] = self.mod_inverse(self.factorial_cache[i], x)
    def compute_prime_factors_count(self, number):
        if number in self.prime_factor_map:
            return
        value = number
        factors = []
        divisor = 2
        while divisor * divisor <= value:
            if value % divisor == 0:
                count = 0
                while value % divisor == 0:
                    count += 1
                    value //= divisor
                factors.append(count)
            divisor += 1
        if value > 1:
            factors.append(1)
        self.prime_factor_map[number] = factors
    def combination(self, total, choose):
        if choose > total or choose < 0:
            return 0
        self.compute_factorial_and_inverse(total)
        return (self.factorial_cache[total] * self.inv_factorial_cache[choose] % x * self.inv_factorial_cache[total - choose] % x)
    def waysToFillArray(self, queries):
        outcomes = []
        for total_elements, k in queries:
            self.compute_prime_factors_count(k)
            total_ways = 1
            for factor_count in self.prime_factor_map[k]:
                total_ways = total_ways * self.combination(factor_count + total_elements - 1, total_elements - 1) % x
            outcomes.append(total_ways)
        return outcomes
