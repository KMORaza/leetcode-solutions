class Solution:
    def maxScoreIndices(self, input_array):
        total_ones_count = sum(input_array)
        total_zeros_count = len(input_array) - total_ones_count
        index_list = [0]
        zeros_left_count = 0
        ones_left_count = 0
        maximum_score = total_ones_count
        for idx in range(len(input_array)):
            zeros_left_count += 1 if input_array[idx] == 0 else 0
            ones_left_count += 1 if input_array[idx] == 1 else 0
            ones_right_count = total_ones_count - ones_left_count
            current_calculated_score = zeros_left_count + ones_right_count
            if maximum_score == current_calculated_score:
                index_list.append(idx + 1)
            elif maximum_score < current_calculated_score:
                maximum_score = current_calculated_score
                index_list = [idx + 1]
        return index_list