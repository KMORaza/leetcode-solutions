class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            chunks = [s[i:i + k] for i in range(0, len(s), k)]
            s = ''.join(str(sum(int(char) for char in chunk)) for chunk in chunks)
        return s