class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True

        for i in range(num):
            reversed_i = int(str(i)[::-1])
            if i + reversed_i == num:
                return True

        return False