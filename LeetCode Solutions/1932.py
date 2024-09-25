class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def canMerge(self, trees):
        node_map = {}
        frequency_count = {}
        for tree in trees:
            node_map[tree.val] = tree
            frequency_count[tree.val] = frequency_count.get(tree.val, 0) + 1
            if tree.left:
                frequency_count[tree.left.val] = frequency_count.get(tree.left.val, 0) + 1
            if tree.right:
                frequency_count[tree.right.val] = frequency_count.get(tree.right.val, 0) + 1
        for tree in trees:
            if frequency_count[tree.val] == 1:
                if self.validateBinarySearchTree(tree, None, None, node_map) and len(node_map) <= 1:
                    return tree
                return None
        return None
    def validateBinarySearchTree(self, current_node, min_limit, max_limit, node_map):
        if not current_node:
            return True
        if min_limit is not None and current_node.val <= min_limit.val:
            return False
        if max_limit is not None and current_node.val >= max_limit.val:
            return False
        if not current_node.left and not current_node.right and current_node.val in node_map:
            val = current_node.val
            current_node.left = node_map[val].left
            current_node.right = node_map[val].right
            del node_map[val]
        return (self.validateBinarySearchTree(current_node.left, min_limit, current_node, node_map) and
                self.validateBinarySearchTree(current_node.right, current_node, max_limit, node_map))
