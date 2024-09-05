class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        MOD = 1337
        MOD1 = 7
        MOD2 = 191
        PHI1 = MOD1 - 1
        PHI2 = MOD2 - 1
        def mod_exp(base, exp, mod):
            result = 1
            base = base % mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                exp = exp >> 1
                base = (base * base) % mod
            return result
        def large_mod(base, exp_list, mod):
            exp = 0
            for digit in exp_list:
                exp = (exp * 10 + digit) % mod
            return exp
        exp_mod1 = large_mod(a, b, PHI1)
        exp_mod2 = large_mod(a, b, PHI2)
        if exp_mod1 == 0:
            exp_mod1 = PHI1
        if exp_mod2 == 0:
            exp_mod2 = PHI2
        part1 = mod_exp(a, exp_mod1, MOD1)
        part2 = mod_exp(a, exp_mod2, MOD2)
        def chinese_remainder_theorem(a1, a2, m1, m2):
            _, inv_m1, _ = self.extended_gcd(m1, m2)
            x = (a1 + (a2 - a1) * inv_m1 % m2 * m1) % (m1 * m2)
            return x
        return chinese_remainder_theorem(part1, part2, MOD1, MOD2)
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        g, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y