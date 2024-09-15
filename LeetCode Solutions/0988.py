class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.min_path = None
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self._explorePaths(root, [])
        return self.min_path if self.min_path is not None else ""
    def _explorePaths(self, node: TreeNode, current_path: list) -> None:
        if node is None:
            return
        current_path.append(chr(node.val + ord('a')))
        if node.left is None and node.right is None:
            candidate_path = ''.join(reversed(current_path))
            if self.min_path is None or self.min_path > candidate_path:
                self.min_path = candidate_path
        self._explorePaths(node.left, current_path)
        self._explorePaths(node.right, current_path)
        current_path.pop()
