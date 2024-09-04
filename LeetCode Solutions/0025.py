class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def countNodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        def reverseKNodes(head, k):
            ptr = head
            for i in range(k):
                if not ptr:
                    return head
                ptr = ptr.next
            prev, curr = None, head
            for i in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            if head:
                head.next = self.reverseKGroup(curr, k)
            return prev
        total_nodes = countNodes(head)
        return reverseKNodes(head, k)
