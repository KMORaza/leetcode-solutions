from math import factorial
from collections import Counter
class Solution:
    def makeStringSorted(self, s: str) -> int:
        N = 10**9 + 7
        count = Counter(s)
        n = len(s)
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % N
        def mod_inv(x):
            return pow(x, N - 2, N)
        ifact = [1] * (n + 1)
        for i in range(2, n + 1):
            ifact[i] = mod_inv(fact[i])
        total_permutations = 0
        for i, char in enumerate(s):
            for smaller_char in sorted(count.keys()):
                if smaller_char >= char:
                    break
                count[smaller_char] -= 1
                remaining = n - i - 1
                permutations = fact[remaining]
                for c in count.values():
                    permutations = permutations * ifact[c] % N
                total_permutations = (total_permutations + permutations) % N
                count[smaller_char] += 1
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        return total_permutations
