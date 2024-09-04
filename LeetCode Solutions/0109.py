from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def listToArray(node: ListNode) -> List[int]:
            array = []
            while node:
                array.append(node.val)
                node = node.next
            return array
        def sortedArrayToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(left, mid - 1)
            root.right = sortedArrayToBST(mid + 1, right)
            return root
        nums = listToArray(head)
        return sortedArrayToBST(0, len(nums) - 1)