import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        prev_count, prev_char = 0, ''
        result = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_char))
            prev_count, prev_char = count + 1, char
        result_str = ''.join(result)
        return result_str if len(result_str) == len(s) else ""
