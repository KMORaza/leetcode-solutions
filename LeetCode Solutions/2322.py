class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Build tree with root 0 and compute necessary values
        parent = [-1] * n
        subtree_xor = [0] * n
        entry_time = [0] * n
        exit_time = [0] * n
        time = 0

        def dfs(u, p):
            nonlocal time
            parent[u] = p
            entry_time[u] = time
            time += 1
            subtree_xor[u] = nums[u]
            for v in graph[u]:
                if v != p:
                    dfs(v, u)
                    subtree_xor[u] ^= subtree_xor[v]
            exit_time[u] = time - 1

        dfs(0, -1)
        total_xor = subtree_xor[0]

        def is_ancestor(a, b):
            return entry_time[a] <= entry_time[b] and exit_time[b] <= exit_time[a]

        min_score = float('inf')

        # Get all edges as (child, parent) pairs
        edge_list = []
        for i in range(1, n):
            edge_list.append((i, parent[i]))

        m = len(edge_list)
        for i in range(m):
            for j in range(i + 1, m):
                u1, p1 = edge_list[i]
                u2, p2 = edge_list[j]

                if is_ancestor(u1, u2):
                    # u1 is ancestor of u2
                    xor_a = subtree_xor[u2]
                    xor_b = subtree_xor[u1] ^ subtree_xor[u2]
                    xor_c = total_xor ^ subtree_xor[u1]
                elif is_ancestor(u2, u1):
                    # u2 is ancestor of u1
                    xor_a = subtree_xor[u1]
                    xor_b = subtree_xor[u2] ^ subtree_xor[u1]
                    xor_c = total_xor ^ subtree_xor[u2]
                else:
                    # Independent subtrees
                    xor_a = subtree_xor[u1]
                    xor_b = subtree_xor[u2]
                    xor_c = total_xor ^ xor_a ^ xor_b

                scores = [xor_a, xor_b, xor_c]
                score = max(scores) - min(scores)
                min_score = min(min_score, score)

        return min_score