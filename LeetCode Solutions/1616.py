class Solution:
    def checkPalindromeFormation(self, first: str, second: str) -> bool:
        return self.validate(first, second) or self.validate(second, first)
    def validate(self, first: str, second: str) -> bool:
        left, right = 0, len(first) - 1
        while left < right:
            if first[left] != second[right]:
                return self.isPalindrome(first, left, right) or self.isPalindrome(second, left, right)
            left += 1
            right -= 1
        return True
    def isPalindrome(self, string: str, start: int, end: int) -> bool:
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True
