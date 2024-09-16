from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        digits = "123456789"
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num_str = digits[start:start + length]
                num = int(num_str)
                if low <= num <= high:
                    result.append(num)
        return sorted(result)
