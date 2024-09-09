class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x1p, y1p, x2p, y2p = rec2
        if x2 <= x1p or x2p <= x1:
            return False
        if y2 <= y1p or y2p <= y1:
            return False
        return True
