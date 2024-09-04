class Solution:
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            result += [x + (1 << i) for x in reversed(result)]
        return result
