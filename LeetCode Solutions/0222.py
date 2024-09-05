class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def get_height(node: TreeNode) -> int:
            height = 0
            while node:
                node = node.left
                height += 1
            return height
        def exists(index: int, height: int, node: TreeNode) -> bool:
            left, right = 0, (1 << height) - 1
            while height > 0:
                mid = (left + right) // 2
                if index <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
                height -= 1
            return node is not None
        height = get_height(root) - 1
        if height < 0:
            return 0
        left, right = 0, (1 << height) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1
        return (1 << height) - 1 + left
