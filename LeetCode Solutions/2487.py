class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        current = head

        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next

        dummy = ListNode(0)
        current = dummy

        for node in stack:
            current.next = node
            current = current.next

        return dummy.next