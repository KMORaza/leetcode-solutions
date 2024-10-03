class CountIntervals:
    class IntervalNode:
        def __init__(self, begin, end):
            self.begin = begin
            self.end = end
            self.covered_length = 0
            self.lazy_value = 0
            self.left = None
            self.right = None
        def midpoint(self):
            return (self.begin + self.end) // 2
    def __init__(self):
        self.root = self.IntervalNode(1, int(1e9))
    def add(self, left, right):
        self._update_range(self.root, left, right)
    def _update_range(self, node, start, end):
        if start > end:
            return
        if node.begin >= start and node.end <= end:
            node.covered_length = node.end - node.begin + 1
            node.lazy_value = 1
            return
        self._push_lazy(node)
        if start <= node.midpoint():
            if not node.left:
                node.left = self.IntervalNode(node.begin, node.midpoint())
            self._update_range(node.left, start, end)
        if end > node.midpoint():
            if not node.right:
                node.right = self.IntervalNode(node.midpoint() + 1, node.end)
            self._update_range(node.right, start, end)
        self._combine(node)
    def count(self):
        return self._query_range(self.root, 1, int(1e9))
    def _query_range(self, node, start, end):
        if start > end:
            return 0
        if node.begin >= start and node.end <= end:
            return node.covered_length
        self._push_lazy(node)
        total = 0
        if start <= node.midpoint() and node.left:
            total += self._query_range(node.left, start, end)
        if end > node.midpoint() and node.right:
            total += self._query_range(node.right, start, end)
        return total
    def _combine(self, node):
        left_length = node.left.covered_length if node.left else 0
        right_length = node.right.covered_length if node.right else 0
        node.covered_length = left_length + right_length
    def _push_lazy(self, node):
        if node.lazy_value != 0:
            if not node.left:
                node.left = self.IntervalNode(node.begin, node.midpoint())
            if not node.right:
                node.right = self.IntervalNode(node.midpoint() + 1, node.end)
            node.left.covered_length = node.left.end - node.left.begin + 1
            node.right.covered_length = node.right.end - node.right.begin + 1
            node.left.lazy_value = 1
            node.right.lazy_value = 1
            node.lazy_value = 0