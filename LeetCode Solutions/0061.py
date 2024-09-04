class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1
        k = k % length
        if k == 0:
            return head
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        last_node.next = head
        return new_head
