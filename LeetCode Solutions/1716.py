class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        extra_days = n % 7
        total = 0
        total += weeks * 28 + (weeks * (weeks - 1) // 2) * 7
        total += (weeks + 1) * extra_days + (extra_days * (extra_days - 1)) // 2
        return total
