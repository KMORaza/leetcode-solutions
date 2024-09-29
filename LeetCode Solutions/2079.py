class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        current_water = capacity
        for i, plant in enumerate(plants):
            if current_water < plant:
                steps += (i * 2)
                current_water = capacity
            current_water -= plant
            steps += 1
        return steps