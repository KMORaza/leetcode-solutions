class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        area = 0
        corner_points = set()
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            area += (x2 - x1) * (y2 - y1)
            corners = {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
            if not corner_points:
                corner_points.update(corners)
            else:
                corner_points.symmetric_difference_update(corners)
        bounding_area = (max_x - min_x) * (max_y - min_y)
        if area != bounding_area:
            return False
        bounding_corners = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return len(corner_points) == 4 and corner_points == bounding_corners
