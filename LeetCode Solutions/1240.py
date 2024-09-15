class Solution:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.coveredRows = []
        self.minTileCount = 0
    def tilingRectangle(self, rectHeight: int, rectWidth: int) -> int:
        self.height = rectHeight
        self.width = rectWidth
        self.minTileCount = rectHeight * rectWidth
        self.coveredRows = [0] * rectHeight
        self.Rectangle(0, 0, 0)
        return self.minTileCount
    def Rectangle(self, r: int, c: int, tilesUsed: int) -> None:
        if c == self.width:
            r += 1
            c = 0
        if r == self.height:
            self.minTileCount = tilesUsed
            return
        if (self.coveredRows[r] >> c & 1) == 1:
            self.Rectangle(r, c + 1, tilesUsed)
        elif tilesUsed + 1 < self.minTileCount:
            maxRowExtent = 0
            maxColExtent = 0
            for i in range(r, self.height):
                if (self.coveredRows[i] >> c & 1) == 1:
                    break
                maxRowExtent += 1
            for j in range(c, self.width):
                if (self.coveredRows[r] >> j & 1) == 1:
                    break
                maxColExtent += 1
            maxSquareSide = min(maxRowExtent, maxColExtent)
            for row in range(r, r + maxSquareSide):
                for col in range(c, c + maxSquareSide):
                    self.coveredRows[row] |= 1 << col
            for size in range(maxSquareSide, 0, -1):
                self.Rectangle(r, c + size, tilesUsed + 1)
                for x in range(size):
                    self.coveredRows[r + size - 1] ^= 1 << (c + x)
                    if x < size - 1:
                        self.coveredRows[r + x] ^= 1 << (c + size - 1)
