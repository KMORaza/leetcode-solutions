class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        first_k_node = head
        for _ in range(k - 1):
            first_k_node = first_k_node.next
        second_k_node = head
        for _ in range(length - k):
            second_k_node = second_k_node.next
        first_k_node.val, second_k_node.val = second_k_node.val, first_k_node.val
        return head
