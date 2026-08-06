# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depths = {}
        heights = {}
        level_max_heights = {}

        def calc_heights(node, depth):
            if not node:
                return -1

            depths[node.val] = depth
            left_h = calc_heights(node.left, depth + 1)
            right_h = calc_heights(node.right, depth + 1)
            h = max(left_h, right_h) + 1
            heights[node.val] = h

            if depth not in level_max_heights:
                level_max_heights[depth] = []
            level_max_heights[depth].append(h)

            return h

        calc_heights(root, 0)

        for depth in level_max_heights:
            level_max_heights[depth].sort(reverse=True)

        result = []
        for q in queries:
            node_depth = depths[q]
            node_height = heights[q]

            candidates = level_max_heights[node_depth]

            if len(candidates) == 1:
                result.append(node_depth - 1)
            else:
                if candidates[0] == node_height:
                    if len(candidates) > 1:
                        result.append(node_depth + candidates[1])
                    else:
                        result.append(node_depth - 1)
                else:
                    result.append(node_depth + candidates[0])

        return result