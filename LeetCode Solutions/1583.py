from typing import List
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        partner = {}
        for a, b in pairs:
            partner[a] = b
            partner[b] = a
        pref_rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for rank, friend in enumerate(preferences[i]):
                pref_rank[i][friend] = rank
        unhappy_count = 0
        for a in range(n):
            b = partner[a]
            for c in preferences[a]:
                if c == b:
                    break
                d = partner[c]
                if pref_rank[c][a] < pref_rank[c][d]:
                    unhappy_count += 1
                    break
        return unhappy_count
