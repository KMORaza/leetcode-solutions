class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next or not head.next.next:
            return
        def find_middle(node):
            slow = fast = node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        def merge_lists(list1, list2):
            while list2:
                temp1 = list1.next
                temp2 = list2.next
                list1.next = list2
                list2.next = temp1
                list1 = temp1
                list2 = temp2
        middle = find_middle(head)
        second_half = middle.next
        middle.next = None
        second_half = reverse_list(second_half)
        merge_lists(head, second_half)
