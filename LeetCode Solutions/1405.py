import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))
        result = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            count = -count
            if result and len(result) >= 2 and result[-1] == result[-2] == char:
                if not max_heap:
                    break
                next_count, next_char = heapq.heappop(max_heap)
                next_count = -next_count
                result.append(next_char)
                next_count -= 1
                if next_count > 0:
                    heapq.heappush(max_heap, (-next_count, next_char))
                heapq.heappush(max_heap, (-count, char))
            else:
                use_count = min(count, 2)
                result.extend(char * use_count)
                count -= use_count
                if count > 0:
                    heapq.heappush(max_heap, (-count, char))
        return ''.join(result)
