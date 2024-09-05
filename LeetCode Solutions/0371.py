class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0xFFFFFFFF
        a, b = a & MAX, b & MAX
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MAX
            b = carry & MAX
        if a > 0x7FFFFFFF:
            a -= (1 << 32)
        return a