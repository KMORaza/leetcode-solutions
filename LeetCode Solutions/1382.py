class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorderTraversal(node):
            if not node:
                return []
            return inorderTraversal(node.left) + [node] + inorderTraversal(node.right)
        def sortedListToBST(nodes):
            if not nodes:
                return None
            mid = len(nodes) // 2
            root = nodes[mid]
            root.left = sortedListToBST(nodes[:mid])
            root.right = sortedListToBST(nodes[mid+1:])
            return root
        sorted_nodes = inorderTraversal(root)
        return sortedListToBST(sorted_nodes)
