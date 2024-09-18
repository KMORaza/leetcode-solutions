from typing import List
import math
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors_sum(n: int) -> int:
            divisors = set()
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    if i != n // i:
                        divisors.add(n // i)
            if len(divisors) == 4:
                return sum(divisors)
            return 0
        total_sum = 0
        for num in nums:
            total_sum += get_divisors_sum(num)
        return total_sum
