from collections import defaultdict
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_count = defaultdict(int)
        def subtree_sum(node):
            if not node:
                return 0
            left_sum = subtree_sum(node.left)
            right_sum = subtree_sum(node.right)
            total_sum = node.val + left_sum + right_sum
            sum_count[total_sum] += 1
            return total_sum
        subtree_sum(root)
        max_freq = max(sum_count.values(), default=0)
        result = [s for s, freq in sum_count.items() if freq == max_freq]
        return result
