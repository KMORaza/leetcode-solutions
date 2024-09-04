class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def split(head):
            if not head or not head.next:
                return head, None
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle
        def merge(left, right):
            dummy = ListNode(0)
            current = dummy
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left if left else right
            return dummy.next
        if not head or not head.next:
            return head
        left, right = split(head)
        left = self.sortList(left)
        right = self.sortList(right)
        return merge(left, right)
