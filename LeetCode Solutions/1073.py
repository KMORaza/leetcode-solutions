from typing import List
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def negabinary_to_decimal(arr):
            decimal_value = 0
            power = 1
            for bit in reversed(arr):
                decimal_value += bit * power
                power *= -2
            return decimal_value
        def decimal_to_negabinary(num):
            if num == 0:
                return [0]
            negabinary = []
            while num != 0:
                num, remainder = divmod(num, -2)
                if remainder < 0:
                    remainder += 2
                    num += 1
                negabinary.append(remainder)
            return negabinary[::-1]
        decimal1 = negabinary_to_decimal(arr1)
        decimal2 = negabinary_to_decimal(arr2)
        sum_decimal = decimal1 + decimal2
        return decimal_to_negabinary(sum_decimal)