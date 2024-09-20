class Solution:
    def sumOfFlooredPairs(self, input_nums):
        maximum_value = max(input_nums)
        count_array = [0] * (maximum_value + 1)
        prefix_sum = [0] * (maximum_value + 1)
        for number in input_nums:
            count_array[number] += 1
        for index in range(1, maximum_value + 1):
            prefix_sum[index] = prefix_sum[index - 1] + count_array[index]
        total_sum = 0
        for current_value in range(1, maximum_value + 1):
            if count_array[current_value] > 0:
                for divisor in range(1, (maximum_value // current_value) + 1):
                    total_sum += count_array[current_value] * divisor * (prefix_sum[min(maximum_value, divisor * current_value + current_value - 1)] - prefix_sum[divisor * current_value - 1])
                    total_sum %= (10**9+7)
        return total_sum