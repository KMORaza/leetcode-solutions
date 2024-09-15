from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_index = {char: index for index, char in enumerate(order)}
        def to_alien_indices(word: str) -> List[int]:
            return [char_to_index[char] for char in word]
        alien_words = [to_alien_indices(word) for word in words]
        return all(alien_words[i] <= alien_words[i + 1] for i in range(len(alien_words) - 1))
