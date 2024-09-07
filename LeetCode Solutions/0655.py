from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))
        height = get_height(root) - 1
        m, n = height + 1, (1 << (height + 1)) - 1
        res = [[""] * n for _ in range(m)]
        queue = deque([(root, 0, (n - 1) // 2)])
        while queue:
            node, row, col = queue.popleft()
            if node:
                res[row][col] = str(node.val)
                if node.left:
                    queue.append((node.left, row + 1, col - (1 << (height - row - 1))))
                if node.right:
                    queue.append((node.right, row + 1, col + (1 << (height - row - 1))))
        return res
