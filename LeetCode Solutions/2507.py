class Solution:
    def smallestValue(self, n: int) -> int:
        def get_prime_sum(num):
            prime_sum = 0
            factor = 2
            temp = num

            while factor * factor <= temp:
                while temp % factor == 0:
                    prime_sum += factor
                    temp //= factor
                factor += 1

            if temp > 1:
                prime_sum += temp

            return prime_sum

        prev = n
        current = get_prime_sum(n)

        while current < prev:
            prev = current
            current = get_prime_sum(current)

        return prev