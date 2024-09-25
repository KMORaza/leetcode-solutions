class Solution:
    def colorTheGrid(self, height: int, width: int) -> int:
        self.height = height
        self.width = width
        self.modulus_value = 1000000007
        self.cache = [[0] * 1024 for _ in range(1000)]
        return self.calculate(0, 0, 0, 0)
    def calculate(self, row: int, col: int, last_mask: int, current_mask: int) -> int:
        if col == self.width:
            return 1
        if self.cache[col][last_mask] != 0:
            return self.cache[col][last_mask]
        if row == self.height:
            return self.calculate(0, col + 1, current_mask, 0)
        total_ways = 0
        for color_option in range(1, 4):
            if self.retrieveColor(last_mask, row) == color_option:
                continue
            if row > 0 and self.retrieveColor(current_mask, row - 1) == color_option:
                continue
            total_ways += self.calculate(row + 1, col, last_mask, self.assignColor(current_mask, row, color_option))
            total_ways %= self.modulus_value
        if row == 0:
            self.cache[col][last_mask] = total_ways
        return total_ways
    def retrieveColor(self, mask: int, row: int) -> int:
        return (mask >> (row * 2)) & 3
    def assignColor(self, mask: int, row: int, color: int) -> int:
        return mask | (color << (row * 2))
