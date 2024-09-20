class Solution:
    def minSwaps(self, input_string: str) -> int:
        count_one = input_string.count('1')
        count_zero = len(input_string) - count_one
        if (count_one - count_zero > 1) or (count_zero - count_one > 1):
            return -1
        if count_one > count_zero:
            return self.calculateSwaps(input_string, '1')
        elif count_zero > count_one:
            return self.calculateSwaps(input_string, '0')
        else:
            return min(self.calculateSwaps(input_string, '1'), self.calculateSwaps(input_string, '0'))
    def calculateSwaps(self, input_string: str, current_char: str) -> int:
        swap_count = 0
        for character in input_string:
            if character != current_char:
                swap_count += 1
            current_char = '0' if current_char == '1' else '1'
        return swap_count // 2
