class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = str(n)
        product = 1
        total_sum = 0
        for digit in digits:
            d = int(digit)
            product *= d
            total_sum += d
        return product - total_sum
