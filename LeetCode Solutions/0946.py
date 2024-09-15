from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return not stack
