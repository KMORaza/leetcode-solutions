class Solution:
    def numWays(self, input_str: str) -> int:
        total_ones = input_str.count('1')
        if total_ones % 3 != 0:
            return 0
        if total_ones == 0:
            length = len(input_str)
            return (length - 1) * (length - 2) // 2 % 1000000007
        first_end = -1
        second_start = -1
        second_end = -1
        third_start = -1
        ones_count = 0
        for index, character in enumerate(input_str):
            if character == '1':
                ones_count += 1
            if first_end == -1 and ones_count == total_ones // 3:
                first_end = index
            elif second_start == -1 and ones_count == total_ones // 3 + 1:
                second_start = index
            if second_end == -1 and ones_count == total_ones // 3 * 2:
                second_end = index
            elif third_start == -1 and ones_count == total_ones // 3 * 2 + 1:
                third_start = index
        return (second_start - first_end) * (third_start - second_end) % 1000000007