from typing import List
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    cost[i][j] = self.calculate_overlap(words[i], words[j])
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = len(words[i])
        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    for j in range(n):
                        if not (mask & (1 << j)):
                            new_mask = mask | (1 << j)
                            new_length = dp[mask][i] + len(words[j]) - cost[i][j]
                            if new_length < dp[new_mask][j]:
                                dp[new_mask][j] = new_length
                                parent[new_mask][j] = i
        last_word = min(range(n), key=lambda i: dp[(1 << n) - 1][i])
        mask = (1 << n) - 1
        superstring = []
        while last_word != -1:
            superstring.append(last_word)
            new_mask = mask ^ (1 << last_word)
            last_word = parent[mask][last_word]
            mask = new_mask
        superstring.reverse()
        result = words[superstring[0]]
        for i in range(1, len(superstring)):
            prev = superstring[i - 1]
            curr = superstring[i]
            overlap = cost[prev][curr]
            result += words[curr][overlap:]
        return result
    def calculate_overlap(self, a: str, b: str) -> int:
        max_overlap = 0
        for i in range(1, len(a) + 1):
            if b.startswith(a[-i:]):
                max_overlap = i
        return max_overlap
