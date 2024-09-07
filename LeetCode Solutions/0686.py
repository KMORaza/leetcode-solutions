class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)
        min_repeats = (len_b + len_a - 1) // len_a
        repeated_a = a * min_repeats
        if b in repeated_a:
            return min_repeats
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 1
        return -1
