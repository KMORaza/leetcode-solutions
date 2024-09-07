import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum_divisors = 1
        sqrt_n = int(math.sqrt(num))
        for i in range(2, sqrt_n + 1):
            if num % i == 0:
                sum_divisors += i
                if i != num // i:
                    sum_divisors += num // i
        return sum_divisors == num
