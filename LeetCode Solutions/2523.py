class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(limit ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, limit + 1, i):
                        is_prime[j] = False

            return [num for num in range(2, limit + 1) if is_prime[num]]

        primes = sieve_of_eratosthenes(right)
        primes_in_range = [p for p in primes if left <= p <= right]

        if len(primes_in_range) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes_in_range) - 1):
            diff = primes_in_range[i + 1] - primes_in_range[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes_in_range[i], primes_in_range[i + 1]]

        return result