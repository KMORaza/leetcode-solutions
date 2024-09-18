class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        mid = len(s) // 2
        first_half = sum(1 for char in s[:mid] if char in vowels)
        second_half = sum(1 for char in s[mid:] if char in vowels)
        return first_half == second_half
