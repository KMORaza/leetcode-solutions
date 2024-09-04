import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        for l in lists:
            if l:
                heapq.heappush(min_heap, (l.val, l))
        dummy = ListNode()
        current = dummy
        while min_heap:
            val, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))
        return dummy.next
