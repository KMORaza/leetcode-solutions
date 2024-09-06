class Solution:
    def lastRemaining(self, n: int) -> int:
        start = 1
        step = 1
        left_to_right = True
        while n > 1:
            if left_to_right or n % 2 == 1:
                start += step
            n //= 2
            step *= 2
            left_to_right = not left_to_right
        return start

