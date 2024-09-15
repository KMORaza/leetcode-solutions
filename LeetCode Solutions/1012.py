class Solution:
    def __init__(self):
        self.digits = [0] * 11
        self.dp = [[None] * (1 << 11) for _ in range(11)]
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.countUniqueDigitIntegers(n)
    def countUniqueDigitIntegers(self, n: int) -> int:
        digit_index = -1
        while n > 0:
            digit_index += 1
            self.digits[digit_index] = n % 10
            n //= 10
        return self.dfs(digit_index, 0, True, True)
    def dfs(self, pos: int, mask: int, leading_zero_mode: bool, is_tight: bool) -> int:
        if pos < 0:
            return 0 if leading_zero_mode else 1
        if not leading_zero_mode and not is_tight and self.dp[pos][mask] is not None:
            return self.dp[pos][mask]
        unique_count = 0
        upper_limit = self.digits[pos] if is_tight else 9
        for i in range(upper_limit + 1):
            if (mask >> i) & 1:
                continue
            if i == 0 and leading_zero_mode:
                unique_count += self.dfs(pos - 1, mask, leading_zero_mode, is_tight and i == upper_limit)
            else:
                unique_count += self.dfs(pos - 1, mask | (1 << i), False, is_tight and i == upper_limit)
        if not leading_zero_mode and not is_tight:
            self.dp[pos][mask] = unique_count
        return unique_count
