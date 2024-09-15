class Solution:
    def stoneGameV(self, values):
        total_stones = len(values)
        cumulative_sums = [0] * (total_stones + 1)
        for i in range(1, total_stones + 1):
            cumulative_sums[i] = cumulative_sums[i - 1] + values[i - 1]
        memoization = [[None] * total_stones for _ in range(total_stones)]
        def computeMaxScore(left_index, right_index):
            if left_index == right_index:
                return 0
            if memoization[left_index][right_index] is not None:
                return memoization[left_index][right_index]
            max_score = 0
            accumulated_sum = 0
            for partition_index in range(left_index, right_index):
                accumulated_sum += values[partition_index]
                remaining_sum = cumulative_sums[right_index + 1] - cumulative_sums[left_index] - accumulated_sum
                if accumulated_sum < remaining_sum:
                    if max_score >= accumulated_sum * 2:
                        continue
                    max_score = max(max_score, accumulated_sum + computeMaxScore(left_index, partition_index))
                elif accumulated_sum > remaining_sum:
                    if max_score >= remaining_sum * 2:
                        break
                    max_score = max(max_score, remaining_sum + computeMaxScore(partition_index + 1, right_index))
                else:
                    max_score = max(max_score, max(accumulated_sum + computeMaxScore(left_index, partition_index), remaining_sum + computeMaxScore(partition_index + 1, right_index)))
            memoization[left_index][right_index] = max_score
            return max_score
        return computeMaxScore(0, total_stones - 1)
