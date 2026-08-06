class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        time = time % cycle_length

        if time <= n - 1:
            return 1 + time
        else:
            return n - (time - (n - 1))