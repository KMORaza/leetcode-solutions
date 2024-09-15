from typing import List, Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.memo = defaultdict(list)
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n in self.memo:
            return self.memo[n]
        if n == 1:
            return [TreeNode(0)]
        result = []
        for left_nodes in range(1, n, 2):
            right_nodes = n - 1 - left_nodes
            left_subtrees = self.allPossibleFBT(left_nodes)
            right_subtrees = self.allPossibleFBT(right_nodes)
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    result.append(root)
        self.memo[n] = result
        return result
