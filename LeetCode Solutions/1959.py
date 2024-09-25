class Solution:
    x = 200000000
    def minSpaceWastedKResizing(self, data_array, resize_limit):
        memo_table = [[None] * (resize_limit + 1) for _ in range(len(data_array))]
        return self._compute_min_waste(data_array, 0, resize_limit, memo_table)
    def _compute_min_waste(self, data_array, index_start, resize_limit, memo_table):
        if index_start == len(data_array):
            return 0
        if resize_limit == -1:
            return self.x
        if memo_table[index_start][resize_limit] is not None:
            return memo_table[index_start][resize_limit]
        minimum_waste = self.x
        accumulated_sum = 0
        largest_element = data_array[index_start]
        for index_end in range(index_start, len(data_array)):
            accumulated_sum += data_array[index_end]
            largest_element = max(largest_element, data_array[index_end])
            waste_calculation = largest_element * (index_end - index_start + 1) - accumulated_sum
            minimum_waste = min(minimum_waste, self._compute_min_waste(data_array, index_end + 1, resize_limit - 1, memo_table) + waste_calculation)
        memo_table[index_start][resize_limit] = minimum_waste
        return minimum_waste
