from collections import deque
class Solution:
    def totalStrength(self, elements):
        length = len(elements)
        smaller_left_indices = [-1] * length
        smaller_right_indices = [length] * length
        index_stack = deque()
        for position in range(length):
            while index_stack and elements[index_stack[-1]] >= elements[position]:
                index_stack.pop()
            if index_stack:
                smaller_left_indices[position] = index_stack[-1]
            index_stack.append(position)
        index_stack.clear()
        for position in range(length - 1, -1, -1):
            while index_stack and elements[index_stack[-1]] > elements[position]:
                index_stack.pop()
            if index_stack:
                smaller_right_indices[position] = index_stack[-1]
            index_stack.append(position)
        large_prime = 10**9+7
        cumulative_sum = [0] * (length + 1)
        for position in range(length):
            cumulative_sum[position + 1] = (cumulative_sum[position] + elements[position]) % large_prime
        total_prefix_sum = [0] * (length + 2)
        for position in range(length + 1):
            total_prefix_sum[position + 1] = (total_prefix_sum[position] + cumulative_sum[position]) % large_prime
        overall_strength = 0
        for position in range(length):
            current_strength = elements[position]
            left_limit = smaller_left_indices[position] + 1
            right_limit = smaller_right_indices[position] - 1
            left_contribution = (position - left_limit + 1) * (total_prefix_sum[right_limit + 2] - total_prefix_sum[position + 1]) % large_prime
            right_contribution = (right_limit - position + 1) * (total_prefix_sum[position + 1] - total_prefix_sum[left_limit]) % large_prime
            overall_strength = (overall_strength + current_strength * ((left_contribution - right_contribution) % large_prime)) % large_prime
        return (overall_strength + large_prime) % large_prime