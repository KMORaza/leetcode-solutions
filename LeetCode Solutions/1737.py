class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        count_a = [0] * 26
        count_b = [0] * 26
        for char in a:
            count_a[ord(char) - ord('a')] += 1
        for char in b:
            count_b[ord(char) - ord('a')] += 1
        total_a = len(a)
        total_b = len(b)
        min_ops = float('inf')
        for i in range(26):
            ops = total_a + total_b - count_a[i] - count_b[i]
            min_ops = min(min_ops, ops)
        min_ops = min(min_ops, total_a, total_b)
        return min_ops
