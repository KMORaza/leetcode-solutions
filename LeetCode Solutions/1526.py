from typing import List
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if not target:
            return 0
        operations = 0
        prev = 0
        for num in target:
            if num > prev:
                operations += num - prev
            prev = num
        return operations
