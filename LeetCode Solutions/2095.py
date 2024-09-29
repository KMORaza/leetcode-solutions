class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = fast = head
        prev = None
        count = 0
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            count += 1
        if prev:
            prev.next = slow.next
        return head
