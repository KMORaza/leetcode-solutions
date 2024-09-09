from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        size = length // k
        extra = length % k
        result = []
        current = head
        for i in range(k):
            part_size = size + (1 if i < extra else 0)
            if part_size == 0:
                result.append(None)
            else:
                part_head = current
                for _ in range(part_size - 1):
                    if current:
                        current = current.next
                if current:
                    next_part = current.next
                    current.next = None
                    current = next_part
                result.append(part_head)
        return result
