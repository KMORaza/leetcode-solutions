import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        def gcd(a, b):
            return math.gcd(a, b)
        current = head
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        return head
