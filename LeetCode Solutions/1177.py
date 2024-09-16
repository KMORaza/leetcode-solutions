class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def char_to_bit(c: str) -> int:
            return 1 << (ord(c) - ord('a'))
        n = len(s)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ char_to_bit(s[i])
        result = []
        for start, end, k in queries:
            substr_xor = prefix_xor[end + 1] ^ prefix_xor[start]
            odd_count = bin(substr_xor).count('1')
            needed_changes = (odd_count // 2)
            result.append(needed_changes <= k)
        return result
