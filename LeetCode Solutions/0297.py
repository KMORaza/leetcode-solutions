class Codec:
    def serialize(self, root):
        def preorder(node):
            if not node:
                values.append('#')
                return
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        values = []
        preorder(root)
        return ','.join(values)
    def deserialize(self, data):
        def build_tree():
            val = next(values)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build_tree()
            node.right = build_tree()
            return node
        values = iter(data.split(','))
        return build_tree()
