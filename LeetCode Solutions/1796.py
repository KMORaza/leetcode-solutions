class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(char) for char in s if char.isdigit()}
        if len(digits) < 2:
            return -1
        sorted_digits = sorted(digits)
        return sorted_digits[-2]
