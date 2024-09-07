class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums, head):
        to_remove = set(nums)
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while prev.next:
            if prev.next.val in to_remove:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next