class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        original = x
        reversed_number = 0
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x //= 10
        return original == reversed_number