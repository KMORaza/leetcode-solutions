class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        reverse_start = prev.next
        curr = reverse_start.next
        for _ in range(right - left):
            next_node = curr.next
            curr.next = prev.next
            prev.next = curr
            reverse_start.next = next_node
            curr = next_node
        return dummy.next
