class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        level = 0
        queue = [root]

        while queue:
            size = len(queue)
            current_level_nodes = []

            for _ in range(size):
                node = queue.pop(0)
                current_level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                values = [node.val for node in current_level_nodes]
                values.reverse()
                for i, node in enumerate(current_level_nodes):
                    node.val = values[i]

            level += 1

        return root