class Solution:
    def maximumANDSum(self, values, slots_count):
        total_elements = 2 * slots_count
        combinations_count = 1 << total_elements
        max_values = [0] * combinations_count
        filled_array = values + [0] * (total_elements - len(values))
        for bitmask in range(1, combinations_count):
            chosen_slots = bin(bitmask).count('1')
            current_position = (chosen_slots + 1) // 2
            for idx in range(total_elements):
                if (bitmask >> idx) & 1:
                    max_values[bitmask] = max(max_values[bitmask], max_values[bitmask ^ (1 << idx)] + (current_position & filled_array[idx]))
        return max_values[combinations_count - 1]