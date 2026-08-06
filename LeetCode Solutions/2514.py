class Solution:
    def countAnagrams(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        words = s.split()

        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result = (result * i) % MOD
            return result

        def mod_inverse(a, mod):
            return pow(a, mod - 2, mod)

        def count_arrangements(word):
            n = len(word)
            fact_n = factorial(n)

            char_count = {}
            for c in word:
                char_count[c] = char_count.get(c, 0) + 1

            denominator = 1
            for count in char_count.values():
                denominator = (denominator * factorial(count)) % MOD

            return (fact_n * mod_inverse(denominator, MOD)) % MOD

        result = 1
        for word in words:
            result = (result * count_arrangements(word)) % MOD

        return result