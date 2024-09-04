class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        def dfs(node, currentPath, currentSum):
            if not node:
                return
            currentPath.append(node.val)
            currentSum += node.val
            if not node.left and not node.right and currentSum == targetSum:
                result.append(list(currentPath))
            dfs(node.left, currentPath, currentSum)
            dfs(node.right, currentPath, currentSum)
            currentPath.pop()
        result = []
        dfs(root, [], 0)
        return result
