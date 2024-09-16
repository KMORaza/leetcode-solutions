class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_map = {0: dummy}
        current = head
        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_map:
                start = prefix_map[prefix_sum]
                node = start.next
                sum = prefix_sum
                while node != current:
                    sum += node.val
                    if node != current:
                        del prefix_map[sum]
                    node = node.next
                start.next = current.next
            else:
                prefix_map[prefix_sum] = current
            current = current.next
        return dummy.next
