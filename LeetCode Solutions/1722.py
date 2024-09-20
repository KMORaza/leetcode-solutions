from typing import List
from collections import defaultdict
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = list(range(len(source)))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for u, v in allowedSwaps:
            parent[find(u)] = find(v)
        groups = defaultdict(list)
        for i in range(len(source)):
            root = find(i)
            groups[root].append(i)
        hamming_distance = 0
        for indices in groups.values():
            source_counter = defaultdict(int)
            target_counter = defaultdict(int)
            for index in indices:
                source_counter[source[index]] += 1
                target_counter[target[index]] += 1
            matches = 0
            for value in source_counter:
                if value in target_counter:
                    matches += min(source_counter[value], target_counter[value])
            hamming_distance += len(indices) - matches
        return hamming_distance
