class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        from collections import defaultdict

        n = len(roads) + 1
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        total_fuel = 0

        def dfs(node, parent):
            nonlocal total_fuel
            people = 1

            for neighbor in graph[node]:
                if neighbor != parent:
                    child_people = dfs(neighbor, node)
                    people += child_people

            if node != 0:
                cars_needed = (people + seats - 1) // seats
                total_fuel += cars_needed

            return people

        dfs(0, -1)
        return total_fuel