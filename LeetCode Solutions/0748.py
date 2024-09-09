from collections import Counter
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def count_letters(s: str) -> Counter:
            count = Counter()
            for char in s:
                if char.isalpha():
                    count[char.lower()] += 1
            return count
        plate_count = count_letters(licensePlate)
        min_length = float('inf')
        result_word = ""
        for word in words:
            word_count = count_letters(word)
            if all(word_count[char] >= plate_count[char] for char in plate_count):
                if len(word) < min_length:
                    min_length = len(word)
                    result_word = word
        return result_word
