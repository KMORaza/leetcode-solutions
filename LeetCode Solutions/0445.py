class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_list(head: ListNode) -> ListNode:
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev
        def add_lists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(0)
            current = dummy
            carry = 0
            while l1 or l2 or carry:
                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0
                total = val1 + val2 + carry
                carry = total // 10
                current.next = ListNode(total % 10)
                current = current.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
            return dummy.next
        l1_reversed = reverse_list(l1)
        l2_reversed = reverse_list(l2)
        result_reversed = add_lists(l1_reversed, l2_reversed)
        final_result = reverse_list(result_reversed)
        return final_result
