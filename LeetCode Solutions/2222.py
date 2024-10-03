class Solution:
    def numberOfWays(self, bit_string: str) -> int:
        combinations = 0
        count_left = [0, 0]
        count_right = [0, 0]
        count_right[0] = bit_string.count('0')
        count_right[1] = len(bit_string) - count_right[0]
        for char in bit_string:
            value = int(char)
            count_right[value] -= 1
            if value == 0:
                combinations += count_left[1] * count_right[1]
            else:
                combinations += count_left[0] * count_right[0]
            count_left[value] += 1
        return combinations