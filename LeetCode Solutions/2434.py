class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suffix = [''] * n
        min_suffix[n - 1] = s[n - 1]

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        result = []
        stack = []
        i = 0

        while i < n:
            stack.append(s[i])

            while stack and (i == n - 1 or stack[-1] <= min_suffix[i + 1]):
                result.append(stack.pop())

            i += 1

        while stack:
            result.append(stack.pop())

        return ''.join(result)