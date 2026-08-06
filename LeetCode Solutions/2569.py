from typing import List

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        tree = [0] * (4 * n)
        lazy = [False] * (4 * n)

        def build(node, l, r):
            if l == r:
                tree[node] = nums1[l]
                return
            m = (l + r) // 2
            build(node * 2, l, m)
            build(node * 2 + 1, m + 1, r)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def push(node, l, r):
            if lazy[node]:
                m = (l + r) // 2
                left = node * 2
                right = node * 2 + 1

                tree[left] = (m - l + 1) - tree[left]
                tree[right] = (r - m) - tree[right]

                lazy[left] = not lazy[left]
                lazy[right] = not lazy[right]

                lazy[node] = False

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                tree[node] = (r - l + 1) - tree[node]
                lazy[node] = not lazy[node]
                return

            push(node, l, r)

            m = (l + r) // 2

            if ql <= m:
                update(node * 2, l, m, ql, qr)

            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        build(1, 0, n - 1)

        ans = sum(nums2)
        ones = tree[1]
        res = []

        for q in queries:
            if q[0] == 1:
                update(1, 0, n - 1, q[1], q[2])

            elif q[0] == 2:
                ans += q[1] * tree[1]

            else:
                res.append(ans)

        return res