class Solution:
    def maximumBinaryString(self, input_str: str) -> str:
        count_zeros = input_str.count('0')
        first_zero_index = input_str.find('0')
        result_list = ['1'] * len(input_str)
        if first_zero_index != -1:
            result_list[first_zero_index + count_zeros - 1] = '0'
        return ''.join(result_list)