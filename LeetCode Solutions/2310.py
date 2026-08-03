class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        if k == 0:
            if num % 10 == 0:
                return 1
            else:
                return -1

        for count in range(1, min(num // k + 1, 11)):
            remaining = num - count * k
            if remaining >= 0 and remaining % 10 == 0:
                return count

        return -1