import bisect
from typing import List, Optional


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        sorted_vals = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_vals.append(node.val)
            inorder(node.right)

        inorder(root)

        answer = []
        n = len(sorted_vals)

        for q in queries:
            idx_right = bisect.bisect_right(sorted_vals, q)
            if idx_right > 0:
                mini = sorted_vals[idx_right - 1]
            else:
                mini = -1

            idx_left = bisect.bisect_left(sorted_vals, q)
            if idx_left < n:
                maxi = sorted_vals[idx_left]
            else:
                maxi = -1

            answer.append([mini, maxi])

        return answer