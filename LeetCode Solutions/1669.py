class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = None
        curr = list1
        for i in range(b + 1):
            if i < a:
                prev = curr
            curr = curr.next
        prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = curr
        return list1
