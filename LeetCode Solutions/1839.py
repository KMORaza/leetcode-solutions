class Solution:
    def longestBeautifulSubstring(self, input_str: str) -> int:
        max_length = 0
        unique_count = 1
        start_index = 0
        for end_index in range(1, len(input_str)):
            current_char = input_str[end_index]
            previous_char = input_str[end_index - 1]
            if current_char >= previous_char:
                if current_char > previous_char:
                    unique_count += 1
                if unique_count == 5:
                    max_length = max(max_length, end_index - start_index + 1)
            else:
                unique_count = 1
                start_index = end_index
        return max_length