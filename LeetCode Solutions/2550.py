class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        result = pow(2, n, MOD) - 2
        return result % MOD