class Solution:
    def countHomogenous(self, s: str) -> int:
        count = 0
        total = 0
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            total = (total + count) % 1000000007
        return total
