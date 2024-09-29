class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        sum_val = 0
        head = head.next
        while head:
            if head.val == 0:
                if sum_val > 0:
                    current.next = ListNode(sum_val)
                    current = current.next
                sum_val = 0
            else:
                sum_val += head.val
            head = head.next
        return dummy.next