class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_palindrome(x: int) -> bool:
            s = str(x)
            return s == s[::-1]
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            if x <= 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True
        def generate_palindromes():
            for length in range(1, 10):
                half_length = (length + 1) // 2
                for i in range(10**(half_length-1), 10**half_length):
                    s = str(i)
                    if length % 2 == 0:
                        pal = int(s + s[::-1])
                    else:
                        pal = int(s + s[-2::-1])
                    if pal >= n:
                        yield pal
        for pal in generate_palindromes():
            if is_prime(pal):
                return pal
