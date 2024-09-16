class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def reverse_inorder(node: TreeNode, acc_sum: int) -> int:
            if not node:
                return acc_sum
            acc_sum = reverse_inorder(node.right, acc_sum)
            node.val += acc_sum
            acc_sum = node.val
            return reverse_inorder(node.left, acc_sum)
        reverse_inorder(root, 0)
        return root
