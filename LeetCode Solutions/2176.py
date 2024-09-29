class Solution:
    def countPairs(self, values, threshold):
        array_size = len(values)
        valid_pair_count = 0
        for first_index in range(array_size):
            for second_index in range(first_index + 1, array_size):
                if values[first_index] == values[second_index] and (first_index * second_index) % threshold == 0:
                    valid_pair_count += 1
        return valid_pair_count