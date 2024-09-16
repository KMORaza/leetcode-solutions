class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        X = 10**9 + 7
        def sieve(n):
            is_prime = [True] * (n + 1)
            p = 2
            while (p * p <= n):
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
                p += 1
            primes = [p for p in range(2, n + 1) if is_prime[p]]
            return primes
        def factorial(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % X
            return res
        primes = sieve(n)
        prime_count = len(primes)
        non_prime_count = n - prime_count
        return (factorial(prime_count) * factorial(non_prime_count)) % X
