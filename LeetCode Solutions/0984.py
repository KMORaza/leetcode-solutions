class Solution:
    def strWithout3a3b(self, count_x: int, count_y: int, char_x: str = 'a', char_y: str = 'b') -> str:
        if count_x < count_y:
            return self.strWithout3a3b(count_y, count_x, char_y, char_x)
        if count_y == 0:
            return char_x * min(count_x, 2)
        max_x = min(count_x, 2)
        max_y = 1 if count_x - max_x >= count_y else 0
        return char_x * max_x + char_y * max_y + self.strWithout3a3b(count_x - max_x, count_y - max_y, char_x, char_y)
