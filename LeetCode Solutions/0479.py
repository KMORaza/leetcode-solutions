class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        kMod = 1337
        upper = 10**n - 1
        lower = 10**(n - 1) - 1
        for i in range(upper, lower, -1):
            cand = self.get_palindrome_candidate(i)
            for j in range(upper, lower, -1):
                if j * j < cand:
                    break
                if cand % j == 0:
                    return cand % kMod
        raise ValueError("Palindrome not found!")
    def get_palindrome_candidate(self, i: int) -> int:
        s = str(i)
        reversed_s = s[::-1]
        palindrome = int(s + reversed_s)
        return palindrome
