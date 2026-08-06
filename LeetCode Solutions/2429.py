class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits_num2 = bin(num2).count('1')
        x = 0
        for i in range(31, -1, -1):
            if bits_num2 == 0:
                break
            if num1 & (1 << i):
                x |= (1 << i)
                bits_num2 -= 1
        for i in range(0, 32):
            if bits_num2 == 0:
                break
            if not (x & (1 << i)) and not (num1 & (1 << i)):
                x |= (1 << i)
                bits_num2 -= 1

        return x