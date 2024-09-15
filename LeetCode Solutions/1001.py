class Solution:
    def __init__(self):
        self.grid_size = 0
        self.active_lamps = set()
        self.rows = {}
        self.columns = {}
        self.diagonal1 = {}
        self.diagonal2 = {}
    def gridIllumination(self, n, lamps, queries):
        self.grid_size = n
        self.active_lamps.clear()
        self.rows.clear()
        self.columns.clear()
        self.diagonal1.clear()
        self.diagonal2.clear()
        for lamp in lamps:
            row, column = lamp
            if (row, column) not in self.active_lamps:
                self.active_lamps.add((row, column))
                self._increment_map(self.rows, row)
                self._increment_map(self.columns, column)
                self._increment_map(self.diagonal1, row - column)
                self._increment_map(self.diagonal2, row + column)
        results = []
        for query in queries:
            row, column = query
            if (self._has_illumination(self.rows, row) or
                self._has_illumination(self.columns, column) or
                self._has_illumination(self.diagonal1, row - column) or
                self._has_illumination(self.diagonal2, row + column)):
                results.append(1)
            else:
                results.append(0)
            for x in range(row - 1, row + 2):
                for y in range(column - 1, column + 2):
                    if 0 <= x < self.grid_size and 0 <= y < self.grid_size:
                        if (x, y) in self.active_lamps:
                            self.active_lamps.remove((x, y))
                            self._decrement_map(self.rows, x)
                            self._decrement_map(self.columns, y)
                            self._decrement_map(self.diagonal1, x - y)
                            self._decrement_map(self.diagonal2, x + y)
        return results
    def _increment_map(self, count_map, key):
        if key in count_map:
            count_map[key] += 1
        else:
            count_map[key] = 1
    def _decrement_map(self, count_map, key):
        if key in count_map:
            count_map[key] -= 1
            if count_map[key] == 0:
                del count_map[key]
    def _has_illumination(self, count_map, key):
        return count_map.get(key, 0) > 0
