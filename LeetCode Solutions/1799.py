class Solution:
    def maxScore(self, array):
        pair_count = len(array) // 2
        dp_table = [[-1] * (1 << (pair_count * 2)) for _ in range(pair_count + 1)]
        return self.calculateMaxScore(array, 1, 0, dp_table)
    def calculateMaxScore(self, array, current_round, bit_vector, dp_table):
        if current_round == len(dp_table):
            return 0
        if dp_table[current_round][bit_vector] != -1:
            return dp_table[current_round][bit_vector]
        best_possible = 0
        for index_a in range(len(array)):
            for index_b in range(index_a + 1, len(array)):
                selected_mask = (1 << index_a) | (1 << index_b)
                if (bit_vector & selected_mask) == 0:
                    current_value = current_round * self.calculateGCD(array[index_a], array[index_b])
                    best_possible = max(best_possible, current_value + self.calculateMaxScore(array, current_round + 1, bit_vector | selected_mask, dp_table))
        dp_table[current_round][bit_vector] = best_possible
        return best_possible
    def calculateGCD(self, x, y):
        return x if y == 0 else self.calculateGCD(y, x % y)
