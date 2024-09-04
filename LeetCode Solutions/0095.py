class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        def generateTrees(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generateTrees(start, i - 1)
                right_trees = generateTrees(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
        return generateTrees(1, n)
def serialize(root):
    if not root:
        return "null"
    return f"{root.val},{serialize(root.left)},{serialize(root.right)}"
