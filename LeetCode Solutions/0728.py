from typing import List
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(number: int) -> bool:
            str_number = str(number)
            for char in str_number:
                digit = int(char)
                if digit == 0 or number % digit != 0:
                    return False
            return True
        result = []
        for number in range(left, right + 1):
            if is_self_dividing(number):
                result.append(number)
        return result
