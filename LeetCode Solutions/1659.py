class Solution:
    def getMaxGridHappiness(self, rows, cols, introverts, extroverts):
        max_masks = 2 ** cols
        dp = [[[[[0] * (extroverts + 1) for _ in range(introverts + 1)] for _ in range(max_masks)] for _ in range(max_masks)] for _ in range(rows * cols)]
        return self._computeHappiness(rows, cols, 0, 0, 0, introverts, extroverts, dp)
    def _calculateCost(self, cols, x, y, intro_mask, extro_mask, happiness_change):
        cost = 0
        if x > 0:
            if (intro_mask & (1 << (cols - 1))) > 0:
                cost += happiness_change - 30
            if (extro_mask & (1 << (cols - 1))) > 0:
                cost += happiness_change + 20
        if y > 0:
            if (intro_mask & 1) > 0:
                cost += happiness_change - 30
            if (extro_mask & 1) > 0:
                cost += happiness_change + 20
        return cost
    def _computeHappiness(self, rows, cols, index, intro_mask, extro_mask, introverts_left, extroverts_left, dp):
        x = index // cols
        y = index % cols
        if x == rows:
            return 0
        if dp[index][intro_mask][extro_mask][introverts_left][extroverts_left] > 0:
            return dp[index][intro_mask][extro_mask][introverts_left][extroverts_left]
        new_intro_mask = (intro_mask << 1) & ((1 << cols) - 1)
        new_extro_mask = (extro_mask << 1) & ((1 << cols) - 1)
        skip_happiness = self._computeHappiness(rows, cols, index + 1, new_intro_mask, new_extro_mask, introverts_left, extroverts_left, dp)
        introvert_happiness = (120 + self._calculateCost(cols, x, y, intro_mask, extro_mask, -30) +
                               self._computeHappiness(rows, cols, index + 1, new_intro_mask | 1, new_extro_mask, introverts_left - 1, extroverts_left, dp)) if introverts_left > 0 else float('-inf')
        extrovert_happiness = (40 + self._calculateCost(cols, x, y, intro_mask, extro_mask, 20) +
                               self._computeHappiness(rows, cols, index + 1, new_intro_mask, new_extro_mask | 1, introverts_left, extroverts_left - 1, dp)) if extroverts_left > 0 else float('-inf')
        dp[index][intro_mask][extro_mask][introverts_left][extroverts_left] = max(skip_happiness, introvert_happiness, extrovert_happiness)
        return dp[index][intro_mask][extro_mask][introverts_left][extroverts_left]
