class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        if n == 0:
            return dominoes
        inf = float('inf')
        left_dist = [inf] * n
        right_dist = [inf] * n
        distance = inf
        for i in range(n):
            if dominoes[i] == 'R':
                distance = 0
            elif dominoes[i] == 'L':
                distance = inf
            elif distance != inf:
                distance += 1
            left_dist[i] = distance
        distance = inf
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                distance = 0
            elif dominoes[i] == 'R':
                distance = inf
            elif distance != inf:
                distance += 1
            right_dist[i] = distance
        result = []
        for i in range(n):
            if left_dist[i] < right_dist[i]:
                result.append('R')
            elif left_dist[i] > right_dist[i]:
                result.append('L')
            else:
                result.append('.')
        return ''.join(result)
