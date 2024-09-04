class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        curr = head
        while curr:
            new_node = curr.next
            new_node.random = curr.random.next if curr.random else None
            curr = new_node.next
        curr = head
        new_head = head.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            curr = curr.next
            if curr:
                new_node.next = curr.next
        return new_head
