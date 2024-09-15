from typing import List
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = [0] * 10
        for digit in digits:
            count[digit] += 1
        total_sum = sum(digit * count[digit] for digit in range(10))
        remainder = total_sum % 3
        def remove_digits(remainder):
            if remainder == 1:
                for d in [1, 4, 7]:
                    if count[d] > 0:
                        count[d] -= 1
                        return True
                needed = 2
                for d in [2, 5, 8]:
                    while count[d] > 0 and needed > 0:
                        count[d] -= 1
                        needed -= 1
                    if needed == 0:
                        return True
            elif remainder == 2:
                for d in [2, 5, 8]:
                    if count[d] > 0:
                        count[d] -= 1
                        return True
                needed = 2
                for d in [1, 4, 7]:
                    while count[d] > 0 and needed > 0:
                        count[d] -= 1
                        needed -= 1
                    if needed == 0:
                        return True
            return False
        if remainder != 0:
            if not remove_digits(remainder):
                return ""
        result = []
        for d in range(9, -1, -1):
            result.extend([str(d)] * count[d])
        if result and result[0] == '0':
            return "0"
        return ''.join(result)
