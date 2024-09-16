from typing import List
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0 or cheeseSlices > tomatoSlices:
            return []
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x
        if x < 0 or y < 0:
            return []
        return [x, y]
