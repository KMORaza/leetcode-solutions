from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return Counter(str(x))
        n_count = count_digits(n)
        power_of_2 = 1
        for _ in range(31):
            if count_digits(power_of_2) == n_count:
                return True
            power_of_2 *= 2
        return False
