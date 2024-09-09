class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if tower[i][j] > 1:
                    excess = (tower[i][j] - 1) / 2
                    tower[i][j] = 1
                    if i + 1 < len(tower):
                        tower[i + 1][j] += excess
                        tower[i + 1][j + 1] += excess
        return min(1, tower[query_row][query_glass])
