class Solution:
    def maxDiff(self, number: int) -> int:
        original_str = str(number)
        highest_str = original_str
        lowest_str = original_str
        for char in original_str:
            if char != '9':
                highest_str = original_str.replace(char, '9')
                break
        if lowest_str[0] != '1':
            lowest_str = lowest_str.replace(lowest_str[0], '1')
        else:
            for i in range(1, len(lowest_str)):
                if lowest_str[i] not in '01':
                    lowest_str = lowest_str.replace(lowest_str[i], '0')
                    break
        return int(highest_str) - int(lowest_str)
