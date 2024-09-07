class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start + end) // 2
        self.value = 0
        self.add = 0
        self.left = None
        self.right = None
class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9))
    def modify(self, l, r, v):
        self._modify(l, r, v, self.root)
    def _modify(self, l, r, v, node):
        if l > r:
            return
        if node.start >= l and node.end <= r:
            node.value = v
            node.add = v
            return
        self._pushdown(node)
        if l <= node.mid:
            self._modify(l, r, v, node.left)
        if r > node.mid:
            self._modify(l, r, v, node.right)
        self._pushup(node)
    def query(self, l, r):
        return self._query(l, r, self.root)
    def _query(self, l, r, node):
        if l > r:
            return 0
        if node.start >= l and node.end <= r:
            return node.value
        self._pushdown(node)
        max_val = 0
        if l <= node.mid:
            max_val = max(max_val, self._query(l, r, node.left))
        if r > node.mid:
            max_val = max(max_val, self._query(l, r, node.right))
        return max_val
    def _pushup(self, node):
        node.value = max(node.left.value if node.left else 0,
                         node.right.value if node.right else 0)
    def _pushdown(self, node):
        if node.left is None:
            node.left = Node(node.start, node.mid)
        if node.right is None:
            node.right = Node(node.mid + 1, node.end)
        if node.add != 0:
            left = node.left
            right = node.right
            left.add = node.add
            right.add = node.add
            left.value = node.add
            right.value = node.add
            node.add = 0
class Solution:
    def fallingSquares(self, positions):
        result = []
        tree = SegmentTree()
        max_height = 0
        for start, width in positions:
            end = start + width - 1
            height = tree.query(start, end) + width
            max_height = max(max_height, height)
            result.append(max_height)
            tree.modify(start, end, height)
        return result
