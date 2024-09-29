class SegmentTree:
    def __init__(self, capacity):
        self.data = [0] * (capacity + 1)
    def increment(self, position, amount):
        while position < len(self.data):
            self.data[position] += amount
            position += self.find_lowbit(position)
    def total(self, position):
        sum_total = 0
        while position > 0:
            sum_total += self.data[position]
            position -= self.find_lowbit(position)
        return sum_total
    @staticmethod
    def find_lowbit(value):
        return value & -value
class Solution:
    def goodTriplets(self, first_array, second_array):
        size = len(first_array)
        triplet_count = 0
        index_lookup = {element: idx for idx, element in enumerate(first_array)}
        transformed_array = [0] * size
        left_smaller_counts = [0] * size
        right_larger_counts = [0] * size
        left_tree = SegmentTree(size)
        right_tree = SegmentTree(size)
        for idx in range(size):
            transformed_array[idx] = index_lookup[second_array[idx]]
        for idx in range(size):
            left_smaller_counts[idx] = left_tree.total(transformed_array[idx])
            left_tree.increment(transformed_array[idx] + 1, 1)
        for idx in range(size - 1, -1, -1):
            right_larger_counts[idx] = right_tree.total(size) - right_tree.total(transformed_array[idx])
            right_tree.increment(transformed_array[idx] + 1, 1)
        for idx in range(size):
            triplet_count += left_smaller_counts[idx] * right_larger_counts[idx]
        return triplet_count
