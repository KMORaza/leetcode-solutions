from collections import defaultdict
import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        char_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_indices[char].append(index)
        def is_subsequence(word: str) -> bool:
            current_index = -1
            for char in word:
                if char not in char_indices:
                    return False
                indices_list = char_indices[char]
                pos = bisect.bisect_right(indices_list, current_index)
                if pos == len(indices_list):
                    return False
                current_index = indices_list[pos]
            return True
        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1
        return count
