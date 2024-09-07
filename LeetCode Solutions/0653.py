from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def in_order_traversal(node: Optional[TreeNode], values: List[int]) -> None:
            if node:
                in_order_traversal(node.left, values)
                values.append(node.val)
                in_order_traversal(node.right, values)
        values = []
        in_order_traversal(root, values)
        left, right = 0, len(values) - 1
        while left < right:
            current_sum = values[left] + values[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        return False
