import random
from bisect import bisect_left
from collections import defaultdict
class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr
        self.number_to_indices = defaultdict(list)
        for i, num in enumerate(arr):
            self.number_to_indices[num].append(i)
    def query(self, left, right, threshold):
        for _ in range(self.x):
            rand_index = random.randint(left, right)
            num = self.arr[rand_index]
            indices = self.number_to_indices[num]
            l = self.first_greater_equal(indices, left)
            r = self.first_greater_equal(indices, right + 1)
            if r - l >= threshold:
                return num
        return -1
    def first_greater_equal(self, A, target):
        idx = bisect_left(A, target)
        return idx
    x = 20