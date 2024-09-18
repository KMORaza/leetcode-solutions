from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
            stack = []
            result = []
            current = root
            while stack or current:
                while current:
                    stack.append(current)
                    current = current.left
                current = stack.pop()
                result.append(current.val)
                current = current.right
            return result
        list1 = inorder_traversal(root1)
        list2 = inorder_traversal(root2)
        merged_list = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        merged_list.extend(list1[i:])
        merged_list.extend(list2[j:])
        return merged_list
