class Solution:
    def appealSum(self, s: str) -> int:
        last_occurrence = {}
        total_appeal = 0
        n = len(s)
        for i in range(n):
            char = s[i]
            last_index = last_occurrence.get(char, -1)
            total_appeal += (i - last_index) * (n - i)
            last_occurrence[char] = i
        return total_appeal
