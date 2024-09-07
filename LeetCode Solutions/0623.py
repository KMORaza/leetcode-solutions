from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        queue = deque([root])
        current_depth = 1
        while queue:
            if current_depth == depth - 1:
                break
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1
        while queue:
            node = queue.popleft()
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = old_left
            node.right.right = old_right
        return root
