class Solution:
    def largestVariance(self, input_str: str) -> int:
        highest_variance = 0
        for char_one in range(ord('a'), ord('z') + 1):
            for char_two in range(ord('a'), ord('z') + 1):
                if char_one != char_two:
                    highest_variance = max(highest_variance, self.compute_difference(input_str, chr(char_one), chr(char_two)))
        return highest_variance
    def compute_difference(self, input_str: str, primary_char: str, secondary_char: str) -> int:
        max_diff = 0
        primary_count = 0
        secondary_count = 0
        previous_secondary_used = False
        for current_char in input_str:
            if current_char != primary_char and current_char != secondary_char:
                continue
            if current_char == primary_char:
                primary_count += 1
            else:
                secondary_count += 1
            if secondary_count > 0:
                max_diff = max(max_diff, primary_count - secondary_count)
            elif secondary_count == 0 and previous_secondary_used:
                max_diff = max(max_diff, primary_count - 1)
            if secondary_count > primary_count:
                primary_count = 0
                secondary_count = 0
                previous_secondary_used = True
        return max_diff
