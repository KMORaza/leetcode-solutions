class Solution:
    def minimumPerimeter(self, targetFruits: int) -> int:
        start, end = 1, 100000
        while start < end:
            midPoint = (start + end) // 2
            if 2 * midPoint * (midPoint + 1) * (2 * midPoint + 1) >= targetFruits:
                end = midPoint
            else:
                start = midPoint + 1
        return start * 8
