class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a'] * n
        k -= n
        for i in range(n - 1, -1, -1):
            if k <= 0:
                break
            add = min(25, k)
            result[i] = chr(97 + add)
            k -= add
        return ''.join(result)
