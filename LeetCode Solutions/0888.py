from typing import List
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        delta = (sumA - sumB) // 2
        aliceSet = set(aliceSizes)
        for candy in bobSizes:
            if (candy + delta) in aliceSet:
                return [candy + delta, candy]
        return []
