class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        diff = abs(endPos - startPos)
        if (k - diff) < 0 or (k - diff) % 2 != 0:
            return 0

        extra_steps = (k - diff) // 2
        right_steps = diff + extra_steps
        left_steps = extra_steps

        if right_steps > k or left_steps > k:
            return 0

        def mod_inverse(a, m):
            return pow(a, m - 2, m)

        numerator = 1
        denominator = 1
        for i in range(right_steps):
            numerator = (numerator * (k - i)) % MOD
            denominator = (denominator * (i + 1)) % MOD

        result = (numerator * mod_inverse(denominator, MOD)) % MOD
        return result