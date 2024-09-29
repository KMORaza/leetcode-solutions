class Solution:
    def minSwaps(self, bit_array):
        total_length = len(bit_array)
        total_ones = sum(1 for bit in bit_array if bit == 1)
        window_ones_count = 0
        max_ones_in_window = 0
        for position in range(total_length * 2):
            if position >= total_ones and bit_array[(position - total_ones) % total_length] == 1:
                window_ones_count -= 1
            if bit_array[position % total_length] == 1:
                window_ones_count += 1
            max_ones_in_window = max(max_ones_in_window, window_ones_count)
        return total_ones - max_ones_in_window
