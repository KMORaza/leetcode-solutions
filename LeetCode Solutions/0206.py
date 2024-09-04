class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode, method='iterative') -> ListNode:
        if method == 'iterative':
            return self.reverseListIterative(head)
        elif method == 'recursive':
            return self.reverseListRecursive(head)
        else:
            raise ValueError("Method must be either 'iterative' or 'recursive'")
    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head  
        head.next = None
        return new_head
def printList(head: ListNode) -> None:
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    sol = Solution()
    reversed_head_iter = sol.reverseList(head, method='iterative')
    print("Reversed list (iterative):")
    printList(reversed_head_iter)
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head_rec = sol.reverseList(head, method='recursive')
    print("Reversed list (recursive):")
    printList(reversed_head_rec)
