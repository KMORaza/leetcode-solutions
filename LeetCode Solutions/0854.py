from collections import deque
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        queue = deque([s1])
        visited = set([s1])
        swaps = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                if current == s2:
                    return swaps
                i = 0
                while i < len(current) and current[i] == s2[i]:
                    i += 1
                for j in range(i + 1, len(current)):
                    if current[j] == s2[i]:
                        swapped = list(current)
                        swapped[i], swapped[j] = swapped[j], swapped[i]
                        swapped_str = ''.join(swapped)
                        if swapped_str == s2:
                            return swaps + 1
                        if swapped_str not in visited:
                            visited.add(swapped_str)
                            queue.append(swapped_str)
            swaps += 1
        return -1
