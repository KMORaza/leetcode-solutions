class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            binary_str = bin(i)[2:]
            if binary_str not in s:
                return False
        return True
