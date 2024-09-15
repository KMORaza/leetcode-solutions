from typing import List
class Solution:
    def maxHeight(self, blocks: List[List[int]]) -> int:
        for b in blocks:
            b.sort()
        blocks.sort(key=lambda x: (x[0], x[1], x[2]))
        m = len(blocks)
        heights = [0] * m
        for i in range(m):
            heights[i] = blocks[i][2]
        for i in range(1, m):
            for j in range(i):
                if blocks[j][0] <= blocks[i][0] and blocks[j][1] <= blocks[i][1] and blocks[j][2] <= blocks[i][2]:
                    heights[i] = max(heights[i], heights[j] + blocks[i][2])
        return max(heights)