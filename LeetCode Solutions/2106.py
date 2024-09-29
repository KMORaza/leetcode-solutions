class Solution:
    def maxTotalFruits(self, fruit_data, starting_position: int, max_steps: int) -> int:
        rightmost_position = max(starting_position, fruit_data[-1][0])
        maximum_fruits = 0
        fruit_counts = [0] * (1 + rightmost_position)
        cumulative_sum = [0] * (2 + rightmost_position)
        for fruit in fruit_data:
            fruit_counts[fruit[0]] = fruit[1]
        for index in range(len(cumulative_sum) - 1):
            cumulative_sum[index + 1] = cumulative_sum[index] + fruit_counts[index]
        max_right_steps = min(rightmost_position - starting_position, max_steps)
        for right_moves in range(max_right_steps + 1):
            left_moves = max(0, max_steps - 2 * right_moves)
            maximum_fruits = max(maximum_fruits, self.calculateFruits(starting_position, rightmost_position, left_moves, right_moves, cumulative_sum))
        max_left_steps = min(starting_position, max_steps)
        for left_moves in range(max_left_steps + 1):
            right_moves = max(0, max_steps - 2 * left_moves)
            maximum_fruits = max(maximum_fruits, self.calculateFruits(starting_position, rightmost_position, left_moves, right_moves, cumulative_sum))
        return maximum_fruits
    def calculateFruits(self, starting_position, rightmost_position, left_moves, right_moves, cumulative_sum):
        left_boundary = max(0, starting_position - left_moves)
        right_boundary = min(rightmost_position, starting_position + right_moves)
        return cumulative_sum[right_boundary + 1] - cumulative_sum[left_boundary]
