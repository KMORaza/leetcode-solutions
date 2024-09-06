import random
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.areas = []
        self.prefix_sum = []
        self.total_area = 0
        for rect in rects:
            x1, y1, x2, y2 = rect
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            self.total_area += area
            self.areas.append(area)
            self.prefix_sum.append(self.total_area)
    def pick(self) -> List[int]:
        rand_area = random.randint(1, self.total_area)
        lo, hi = 0, len(self.prefix_sum) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.prefix_sum[mid] < rand_area:
                lo = mid + 1
            else:
                hi = mid
        rect_index = lo
        rect = self.rects[rect_index]
        x1, y1, x2, y2 = rect
        if rect_index == 0:
            offset = rand_area
        else:
            offset = rand_area - self.prefix_sum[rect_index - 1]
        width = x2 - x1 + 1
        height = y2 - y1 + 1
        random_x = x1 + (offset - 1) % width
        random_y = y1 + (offset - 1) // width
        return [random_x, random_y]
