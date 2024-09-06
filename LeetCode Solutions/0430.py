class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
class Solution:
    def flatten(self, head: Node) -> Node:
        def flatten_and_return_tail(node):
            if not node:
                return None
            current = node
            last = None
            while current:
                next_node = current.next
                if current.child:
                    child_tail = flatten_and_return_tail(current.child)
                    current.next = current.child
                    current.child.prev = current
                    current.child = None
                    if child_tail:
                        child_tail.next = next_node
                    if next_node:
                        next_node.prev = child_tail
                    last = child_tail
                else:
                    last = current
                current = next_node
            return last
        flatten_and_return_tail(head)
        return head
#------- Testing -------#
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
head.next.next.next = Node(4)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.prev = head.next.next.next.next
head.next.child = Node(7)
head.next.child.next = Node(8)
head.next.child.next.prev = head.next.child
head.next.child.next.next = Node(9)
head.next.child.next.next.prev = head.next.child.next
head.next.child.next.next.next = Node(10)
head.next.child.next.next.next.prev = head.next.child.next.next
head.next.child.child = Node(11)
head.next.child.child.next = Node(12)
head.next.child.child.next.prev = head.next.child.child
solution = Solution()
flattened_head = solution.flatten(head)
current = flattened_head
while current:
    print(current.val, end=' ')
    current = current.next
