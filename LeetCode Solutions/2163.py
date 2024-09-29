import heapq
class Solution:
    def minimumDifference(self, input_array):
        array_length = len(input_array)
        partition_size = array_length // 3
        prefix_sum_list = [0] * (array_length + 1)
        max_priority_queue = []
        cumulative_sum = 0
        for index in range(1, partition_size * 2 + 1):
            current_value = input_array[index - 1]
            cumulative_sum += current_value
            heapq.heappush(max_priority_queue, -current_value)
            if len(max_priority_queue) > partition_size:
                cumulative_sum += heapq.heappop(max_priority_queue)
            prefix_sum_list[index] = cumulative_sum
        cumulative_sum = 0
        suffix_sum_list = [0] * (array_length + 1)
        min_priority_queue = []
        for index in range(array_length, partition_size, -1):
            current_value = input_array[index - 1]
            cumulative_sum += current_value
            heapq.heappush(min_priority_queue, current_value)
            if len(min_priority_queue) > partition_size:
                cumulative_sum -= heapq.heappop(min_priority_queue)
            suffix_sum_list[index] = cumulative_sum
        minimum_difference = float('inf')
        for index in range(partition_size, partition_size * 2 + 1):
            minimum_difference = min(minimum_difference, prefix_sum_list[index] - suffix_sum_list[index + 1])
        return minimum_difference
