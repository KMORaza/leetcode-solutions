class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        num_set = set(nums)
        in_component = False
        component_count = 0
        current = head
        while current:
            if current.val in num_set:
                if not in_component:
                    component_count += 1
                    in_component = True
            else:
                in_component = False
            current = current.next
        return component_count
