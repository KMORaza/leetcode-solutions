import random
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total_cells = m * n
        self.flipped_cells = {}
        self.available_count = self.total_cells
    def flip(self):
        rand_index = random.randint(0, self.available_count - 1)
        i, j = divmod(rand_index, self.n)
        if rand_index in self.flipped_cells:
            while rand_index in self.flipped_cells:
                rand_index = (rand_index + 1) % self.total_cells
                i, j = divmod(rand_index, self.n)
        self.flipped_cells[rand_index] = (i, j)
        self.available_count -= 1
        return [i, j]
    def reset(self):
        self.flipped_cells.clear()
        self.available_count = self.total_cells
