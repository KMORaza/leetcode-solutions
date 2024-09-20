from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        total_units = 0
        for boxes, units in boxTypes:
            if truckSize <= 0:
                break
            take_boxes = min(boxes, truckSize)
            total_units += take_boxes * units
            truckSize -= take_boxes
        return total_units