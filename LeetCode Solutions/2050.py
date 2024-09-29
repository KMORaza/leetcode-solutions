from typing import List, DefaultDict
from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = DefaultDict(list)
        indegree = [0] * n
        for pre, task in relations:
            graph[pre - 1].append(task - 1)
            indegree[task - 1] += 1
        dp = [0] * n
        for i in range(n):
            dp[i] = time[i]
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                dp[neighbor] = max(dp[neighbor], dp[curr] + time[neighbor])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return max(dp)
