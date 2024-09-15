class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        total_cost = 0
        current_level = 0
        for used, required in tasks:
            if current_level < required:
                total_cost += required - current_level
                current_level = required
            current_level -= used
        return total_cost
