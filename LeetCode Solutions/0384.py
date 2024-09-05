import random
class Solution:
    def __init__(self, nums: list[int]):
        self.original = nums[:]
        self.array = nums
    def reset(self) -> list[int]:
        return self.original
    def shuffle(self) -> list[int]:
        shuffled = self.array[:]
        n = len(shuffled)
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
