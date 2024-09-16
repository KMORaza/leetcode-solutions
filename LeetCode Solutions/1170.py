from typing import List
import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def smallest_char_frequency(s: str) -> int:
            smallest_char = min(s)
            return s.count(smallest_char)
        word_freqs = [smallest_char_frequency(word) for word in words]
        word_freqs.sort()
        result = []
        for query in queries:
            query_freq = smallest_char_frequency(query)
            count_greater = len(word_freqs) - bisect.bisect_right(word_freqs, query_freq)
            result.append(count_greater)
        return result
