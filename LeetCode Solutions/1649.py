class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        X = 10**9 + 7
        max_val = max(instructions)
        bit = [0] * (max_val + 1)
        def update(index, delta):
            while index <= max_val:
                bit[index] += delta
                index += index & -index
        def query(index):
            result = 0
            while index > 0:
                result += bit[index]
                index -= index & -index
            return result
        total_cost = 0
        for num in instructions:
            less_count = query(num - 1)
            greater_count = query(max_val) - query(num)
            cost = min(less_count, greater_count)
            total_cost = (total_cost + cost) % X
            update(num, 1)
        return total_cost