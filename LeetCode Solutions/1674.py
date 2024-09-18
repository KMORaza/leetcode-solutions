class Solution:
    def minMoves(self, data, threshold):
        num_pairs = len(data) // 2
        adjustments = [0] * (threshold * 2 + 2)
        for i in range(num_pairs):
            lower = min(data[i], data[len(data) - i - 1])
            upper = max(data[i], data[len(data) - i - 1])
            adjustments[2] += 2
            adjustments[threshold * 2 + 1] -= 2
            adjustments[lower + 1] -= 1
            adjustments[upper + threshold + 1] += 1
            adjustments[lower + upper] -= 1
            adjustments[lower + upper + 1] += 1
        min_steps = num_pairs * 2
        current_steps = 0
        for total_sum in range(2, threshold * 2 + 1):
            current_steps += adjustments[total_sum]
            if current_steps < min_steps:
                min_steps = current_steps
        return min_steps