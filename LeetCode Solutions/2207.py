class Solution:
    def maximumSubsequenceCount(self, source_string: str, search_pattern: str) -> int:
        subsequence_total = 0
        first_char_tracker = 0
        second_char_tracker = 0
        for current_char in source_string:
            if current_char == search_pattern[1]:
                subsequence_total += first_char_tracker
                second_char_tracker += 1
            if current_char == search_pattern[0]:
                first_char_tracker += 1
        return subsequence_total + max(first_char_tracker, second_char_tracker)