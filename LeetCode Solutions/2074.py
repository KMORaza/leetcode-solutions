class ListNode:
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node
class Solution:
    def reverseEvenLengthGroups(self, start_node: ListNode) -> ListNode:
        placeholder = ListNode(0, start_node)
        prior = placeholder
        current_end = start_node
        following_node = start_node.next if start_node else None
        size_of_group = 1
        while True:
            if size_of_group % 2 == 1:
                prior.next = start_node
                prior = current_end
            else:
                current_end.next = None
                prior.next = self.reverse_segment(start_node)
                start_node.next = following_node
                prior = start_node
            if following_node is None:
                break
            start_node = following_node
            current_end, calculated_length = self.calculate_tail_and_length(start_node, size_of_group + 1)
            following_node = current_end.next if current_end else None
            size_of_group = calculated_length
        return placeholder.next
    def calculate_tail_and_length(self, current_start: ListNode, size_of_group: int):
        length_counter = 1
        current_end = current_start
        while length_counter < size_of_group and current_end.next:
            current_end = current_end.next
            length_counter += 1
        return current_end, length_counter
    def reverse_segment(self, current_start: ListNode):
        previous_node = None
        while current_start:
            next_node = current_start.next
            current_start.next = previous_node
            previous_node = current_start
            current_start = next_node
        return previous_node
