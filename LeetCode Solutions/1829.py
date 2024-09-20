class Solution:
    def getMaximumXor(self, input_nums, bit_limit):
        total_xor = 0
        for number in input_nums:
            total_xor ^= number
        bitmask = (1 << bit_limit) - 1
        array_length = len(input_nums)
        result_xors = [0] * array_length
        for index in range(array_length):
            max_xor_value = total_xor ^ bitmask
            result_xors[index] = max_xor_value
            current_number = input_nums[array_length - index - 1]
            total_xor ^= current_number
        return result_xors
