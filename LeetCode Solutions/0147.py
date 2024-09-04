class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float('-inf'))
        current = head
        while current:
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            next_to_process = current.next
            current.next = prev.next
            prev.next = current
            current = next_to_process
        return dummy.next
