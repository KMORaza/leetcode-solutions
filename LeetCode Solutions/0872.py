class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSequence(node: Optional[TreeNode]) -> List[int]:
            leaves = []
            stack = [node]
            while stack:
                current = stack.pop()
                if not current:
                    continue
                if not current.left and not current.right:
                    leaves.append(current.val)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
            return leaves
        leaves1 = getLeafSequence(root1)
        leaves2 = getLeafSequence(root2)
        return leaves1 == leaves2
