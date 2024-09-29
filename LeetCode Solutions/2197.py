from typing import List
from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                last = stack.pop()
                num = (last * num) // gcd(last, num)
            stack.append(num)
        return stack
