class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x_str = str(x)
        if n[0] == '-':
            for i in range(1, len(n) + 1):
                if n[i - 1] > x_str:
                    return n[:i - 1] + x_str + n[i - 1:]
            return n + x_str
        else:
            for i in range(len(n)):
                if n[i] < x_str:
                    return n[:i] + x_str + n[i:]
            return n + x_str