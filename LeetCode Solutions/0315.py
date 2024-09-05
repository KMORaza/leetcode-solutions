class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_unique_nums = sorted(set(nums))
        rank = {num: i + 1 for i, num in enumerate(sorted_unique_nums)}
        bit = BIT(len(sorted_unique_nums))
        result = []
        for num in reversed(nums):
            smaller_count = bit.query(rank[num] - 1)
            result.append(smaller_count)
            bit.update(rank[num], 1)
        return result[::-1]

