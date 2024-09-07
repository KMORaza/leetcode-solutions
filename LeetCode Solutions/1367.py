class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isSubPathFrom(root: Optional[TreeNode], head: Optional[ListNode]) -> bool:
            if not head:
                return True
            if not root:
                return False
            if root.val != head.val:
                return False
            return (isSubPathFrom(root.left, head.next) or
                    isSubPathFrom(root.right, head.next))
        def dfs(root: Optional[TreeNode], head: Optional[ListNode]) -> bool:
            if not root:
                return False
            if isSubPathFrom(root, head):
                return True
            return dfs(root.left, head) or dfs(root.right, head)
        return dfs(root, head)
