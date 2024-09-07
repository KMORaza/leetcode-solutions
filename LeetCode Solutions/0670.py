class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_occurrence = {int(d): i for i, d in enumerate(digits)}
        for i, d in enumerate(digits):
            current_digit = int(d)
            for larger_digit in range(9, current_digit, -1):
                if larger_digit in last_occurrence and last_occurrence[larger_digit] > i:
                    j = last_occurrence[larger_digit]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(digits))
        return num
