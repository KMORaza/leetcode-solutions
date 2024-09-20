class Solution:
    def maxBuilding(self, total_count: int, height_constraints: list[list[int]]) -> int:
        boundary_conditions = [[1, 0]]
        boundary_conditions.extend(height_constraints)
        boundary_conditions.sort(key=lambda x: x[0])
        if boundary_conditions[-1][0] != total_count:
            boundary_conditions.append([total_count, total_count - 1])
        condition_count = len(boundary_conditions)
        for index in range(1, condition_count):
            previous_limit = boundary_conditions[index - 1]
            current_limit = boundary_conditions[index]
            current_limit[1] = min(current_limit[1], previous_limit[1] + current_limit[0] - previous_limit[0])
        for index in range(condition_count - 2, -1, -1):
            current_limit = boundary_conditions[index]
            next_limit = boundary_conditions[index + 1]
            current_limit[1] = min(current_limit[1], next_limit[1] + next_limit[0] - current_limit[0])
        max_possible_height = 0
        for index in range(condition_count - 1):
            current_limit = boundary_conditions[index]
            next_limit = boundary_conditions[index + 1]
            interim_max_height = (current_limit[1] + next_limit[1] + next_limit[0] - current_limit[0]) // 2
            max_possible_height = max(max_possible_height, interim_max_height)
        return max_possible_height
