import random
from collections import defaultdict
class Solution:
    def __init__(self, nums):
        self.num_to_indices = defaultdict(list)
        for index, num in enumerate(nums):
            self.num_to_indices[num].append(index)
    def pick(self, target):
        indices = self.num_to_indices[target]
        return random.choice(indices)
