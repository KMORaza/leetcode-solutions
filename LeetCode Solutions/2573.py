from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        mp = {}
        s = [''] * n
        chars = "abcdefghijklmnopqrstuvwxyz"

        idx = 0

        for i in range(n):
            root = find(i)
            if root not in mp:
                if idx == 26:
                    return ""
                mp[root] = chars[idx]
                idx += 1
            s[i] = mp[root]

        s = ''.join(s)

        for i in range(n):
            for j in range(n):
                k = 0
                while i + k < n and j + k < n and s[i + k] == s[j + k]:
                    k += 1
                if k != lcp[i][j]:
                    return ""

        return s