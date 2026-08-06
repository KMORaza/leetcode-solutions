class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        result = []

        for a, b in queries:
            path_a = []
            path_b = []

            temp = a
            while temp != 0:
                path_a.append(temp)
                temp //= 2

            temp = b
            while temp != 0:
                path_b.append(temp)
                temp //= 2

            path_a.reverse()
            path_b.reverse()

            lca_depth = 0
            min_len = min(len(path_a), len(path_b))

            for i in range(min_len):
                if path_a[i] == path_b[i]:
                    lca_depth = i
                else:
                    break

            depth_a = len(path_a) - 1
            depth_b = len(path_b) - 1
            lca_level = lca_depth

            cycle_length = (depth_a - lca_level) + (depth_b - lca_level) + 1
            result.append(cycle_length)

        return result