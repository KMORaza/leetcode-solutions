from typing import List
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        unique_representations = set()
        for word in words:
            even_chars = word[0::2]
            odd_chars = word[1::2]
            sorted_even_chars = ''.join(sorted(even_chars))
            sorted_odd_chars = ''.join(sorted(odd_chars))
            representation = (sorted_even_chars, sorted_odd_chars)
            unique_representations.add(representation)
        return len(unique_representations)
