class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        palindrome = list(palindrome)
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[-1] = 'b'
        return ''.join(palindrome)
