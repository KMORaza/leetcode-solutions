class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def is_palindrome_in_base(num, base):
            digits = []
            while num:
                digits.append(num % base)
                num //= base
            return digits == digits[::-1]

        for base in range(2, n - 1):
            if not is_palindrome_in_base(n, base):
                return False
        return True