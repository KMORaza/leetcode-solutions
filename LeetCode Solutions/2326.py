from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        matrix = [[-1] * n for _ in range(m)]
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        index = 0
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                if index < len(values):
                    matrix[top][col] = values[index]
                    index += 1
            top += 1
            for row in range(top, bottom + 1):
                if index < len(values):
                    matrix[row][right] = values[index]
                    index += 1
            right -= 1
            for col in range(right, left - 1, -1):
                if index < len(values):
                    matrix[bottom][col] = values[index]
                    index += 1
            bottom -= 1
            for row in range(bottom, top - 1, -1):
                if index < len(values):
                    matrix[row][left] = values[index]
                    index += 1
            left += 1
        return matrix
