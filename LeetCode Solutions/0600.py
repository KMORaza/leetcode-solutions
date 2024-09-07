class Solution:
    def findIntegers(self, num: int) -> int:
        bits = []
        while num > 0:
            bits.append(num & 1)
            num >>= 1
        n = len(bits)
        zero = [0] * n
        one = [0] * n
        zero[0] = 1
        one[0] = 1
        for i in range(1, n):
            zero[i] = zero[i - 1] + one[i - 1]
            one[i] = zero[i - 1]
        ans = zero[n - 1] + one[n - 1]
        for i in range(n - 2, -1, -1):
            if bits[i] == 1 and bits[i + 1] == 1:
                break
            if bits[i] == 0 and bits[i + 1] == 0:
                ans -= one[i]
        return ans
