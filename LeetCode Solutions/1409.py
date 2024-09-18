from typing import List
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        perm = list(range(1, m + 1))
        position = {num: idx for idx, num in enumerate(perm)}
        result = []
        for query in queries:
            idx = position[query]
            result.append(idx)
            perm.pop(idx)
            perm.insert(0, query)
            for i, num in enumerate(perm):
                position[num] = i
        return result
