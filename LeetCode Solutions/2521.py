class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def get_prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        all_primes = set()
        for num in nums:
            all_primes.update(get_prime_factors(num))

        return len(all_primes)