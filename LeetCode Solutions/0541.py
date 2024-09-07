class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        result = []
        for i in range(0, n, 2 * k):
            chunk = s[i:i + 2 * k]
            first_part = chunk[:k][::-1]
            second_part = chunk[k:]
            result.append(first_part + second_part)
        return ''.join(result)

