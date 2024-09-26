class Solution:
    x = 10**9+7
    def numberOfCombinations(self, num_str: str) -> int:
        total_length = len(num_str)
        lcp_matrix = [[0] * (total_length + 1) for _ in range(total_length + 1)]
        for idx_a in range(total_length - 1, -1, -1):
            for idx_b in range(total_length - 1, -1, -1):
                if num_str[idx_a] == num_str[idx_b]:
                    lcp_matrix[idx_a][idx_b] = 1 + lcp_matrix[idx_a + 1][idx_b + 1]
        partition_count = [[0] * (total_length + 1) for _ in range(total_length + 1)]
        partition_count[0][0] = 1
        for end_idx in range(1, total_length + 1):
            for size_idx in range(1, end_idx + 1):
                valid_partition = 0
                if num_str[end_idx - size_idx] != '0':
                    if end_idx >= 2 * size_idx:
                        common_length = lcp_matrix[end_idx - size_idx][end_idx - 2 * size_idx]
                        if (common_length >= size_idx or
                                num_str[end_idx - size_idx + common_length] >= num_str[end_idx - 2 * size_idx + common_length]):
                            valid_partition = partition_count[end_idx - size_idx][size_idx]
                    if valid_partition == 0:
                        valid_partition = partition_count[end_idx - size_idx][min(size_idx - 1, end_idx - size_idx)]
                partition_count[end_idx][size_idx] = (partition_count[end_idx][size_idx - 1] + valid_partition) % self.x
        return partition_count[total_length][total_length]
