class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        X = 10**9 + 7
        def subtree_sums(node):
            if not node:
                return 0
            left_sum = subtree_sums(node.left)
            right_sum = subtree_sums(node.right)
            subtree_sum = node.val + left_sum + right_sum
            subtree_sums_set.add(subtree_sum)
            return subtree_sum
        subtree_sums_set = set()
        total_sum = subtree_sums(root)
        max_product = 0
        for s in subtree_sums_set:
            product = s * (total_sum - s)
            max_product = max(max_product, product)
        return max_product % X
