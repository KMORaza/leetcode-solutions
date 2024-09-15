class Solution:
    def closestToTarget(self, numbers, target):
        import sys
        min_difference = sys.maxsize
        previous_values = set()
        for current_number in numbers:
            current_values = {current_number}
            for previous_value in previous_values:
                current_values.add(previous_value & current_number)
            for value in current_values:
                min_difference = min(min_difference, abs(target - value))
            previous_values = current_values
        return min_difference
