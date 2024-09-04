class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_than_x_head = ListNode(0)
        greater_or_equal_x_head = ListNode(0)
        less_than_x = less_than_x_head
        greater_or_equal_x = greater_or_equal_x_head
        current = head
        while current:
            if current.val < x:
                less_than_x.next = current
                less_than_x = less_than_x.next
            else:
                greater_or_equal_x.next = current
                greater_or_equal_x = greater_or_equal_x.next
            current = current.next
        greater_or_equal_x.next = None
        less_than_x.next = greater_or_equal_x_head.next
        return less_than_x_head.next
