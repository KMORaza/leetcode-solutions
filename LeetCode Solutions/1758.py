class Solution:
    def minOperations(self, s: str) -> int:
        count0 = count1 = 0
        n = len(s)
        for i in range(n):
            expected_char = '0' if i % 2 == 0 else '1'
            if s[i] != expected_char:
                count0 += 1
            expected_char = '1' if i % 2 == 0 else '0'
            if s[i] != expected_char:
                count1 += 1
        return min(count0, count1)
