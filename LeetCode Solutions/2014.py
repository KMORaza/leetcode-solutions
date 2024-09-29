from collections import deque
from typing import List
class Solution:
    def longestSubsequenceRepeatedK(self, string_input: str, occurrence_count: int) -> str:
        longest_sequence = ""
        frequency_array = [0] * 26
        eligible_characters = []
        subsequence_queue = deque([""])
        for char in string_input:
            frequency_array[ord(char) - ord('a')] += 1
        for idx in range(26):
            if frequency_array[idx] >= occurrence_count:
                eligible_characters.append(chr(idx + ord('a')))
        while subsequence_queue:
            current_sequence = subsequence_queue.popleft()
            if len(current_sequence) * occurrence_count > len(string_input):
                return longest_sequence
            for char in eligible_characters:
                new_sequence = current_sequence + char
                if self.check_subsequence(new_sequence, string_input, occurrence_count):
                    subsequence_queue.append(new_sequence)
                    longest_sequence = new_sequence
        return longest_sequence
    def check_subsequence(self, candidate: str, string_input: str, occurrence_count: int) -> bool:
        candidate_index = 0
        for char in string_input:
            if char == candidate[candidate_index]:
                candidate_index += 1
                if candidate_index == len(candidate):
                    occurrence_count -= 1
                    if occurrence_count == 0:
                        return True
                    candidate_index = 0
        return False
