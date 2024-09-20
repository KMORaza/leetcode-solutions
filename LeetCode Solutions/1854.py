from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_change = [0] * 2051
        for birth, death in logs:
            population_change[birth] += 1
            population_change[death] -= 1
        max_population = 0
        current_population = 0
        max_year = 1950
        for year in range(1950, 2051):
            current_population += population_change[year]
            if current_population > max_population:
                max_population = current_population
                max_year = year
        return max_year