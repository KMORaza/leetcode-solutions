class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        def generate_palindromes(limit: int) -> list:
            palindromes = []
            for length in range(1, 11):
                half_length = (length + 1) // 2
                start = 10**(half_length - 1)
                end = 10**half_length
                for half in range(start, end):
                    half_str = str(half)
                    if length % 2 == 0:
                        pal = int(half_str + half_str[::-1])
                    else:
                        pal = int(half_str + half_str[-2::-1])
                    if pal <= limit:
                        palindromes.append(pal)
                    else:
                        break
            return palindromes
        left_int = int(left)
        right_int = int(right)
        limit = int(right_int**0.5) + 1
        palindromes = generate_palindromes(limit)
        count = 0
        for pal in palindromes:
            square = pal * pal
            if square > right_int:
                break
            if square >= left_int and is_palindrome(str(square)):
                count += 1
        return count
