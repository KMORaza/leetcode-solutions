class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left_depths = dfs(node.left)
            right_depths = dfs(node.right)
            for ld in left_depths:
                for rd in right_depths:
                    if ld + rd <= distance:
                        self.result += 1
            return [d + 1 for d in left_depths + right_depths]
        dfs(root)
        return self.result
