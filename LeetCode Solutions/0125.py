import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return filtered_s == filtered_s[::-1]
