class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        from collections import defaultdict

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        guess_set = set()
        for u, v in guesses:
            guess_set.add((u, v))

        n = len(edges) + 1
        correct_guesses = [0] * n

        def dfs1(node, parent):
            count = 0
            for neighbor in graph[node]:
                if neighbor != parent:
                    count += dfs1(neighbor, node)
                    if (node, neighbor) in guess_set:
                        count += 1
            return count

        def reroot_dfs(node, parent, parent_correct):
            total = parent_correct
            if parent != -1 and (parent, node) in guess_set:
                total -= 1
            if parent != -1 and (node, parent) in guess_set:
                total += 1

            correct_guesses[node] = total

            for neighbor in graph[node]:
                if neighbor != parent:
                    reroot_dfs(neighbor, node, total)

        initial_root_correct = dfs1(0, -1)
        correct_guesses[0] = initial_root_correct
        reroot_dfs(0, -1, initial_root_correct)

        result = 0
        for count in correct_guesses:
            if count >= k:
                result += 1

        return result