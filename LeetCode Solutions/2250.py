from bisect import bisect_left
from typing import List
class Solution:
    def countRectangles(self, shapeList: List[List[int]], queryPoints: List[List[int]]) -> List[int]:
        rectangleCount = [0] * len(queryPoints)
        y_to_x_map = [[] for _ in range(101)]
        for shape in shapeList:
            y_to_x_map[shape[1]].append(shape[0])
        for xCoordList in y_to_x_map:
            xCoordList.sort()
        for idx, point in enumerate(queryPoints):
            totalCount = 0
            for y in range(point[1], 101):
                xCoordList = y_to_x_map[y]
                totalCount += len(xCoordList) - bisect_left(xCoordList, point[0])
            rectangleCount[idx] = totalCount
        return rectangleCount
