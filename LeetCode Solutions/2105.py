from typing import List
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        left, right = 0, len(plants) - 1
        refills = 0
        currentA, currentB = capacityA, capacityB
        while left <= right:
            if left == right:
                if currentA >= plants[left] or currentB >= plants[right]:
                    break
                else:
                    refills += 1
                    break
            if currentA < plants[left]:
                refills += 1
                currentA = capacityA
            currentA -= plants[left]
            left += 1
            if currentB < plants[right]:
                refills += 1
                currentB = capacityB
            currentB -= plants[right]
            right -= 1
        return refills