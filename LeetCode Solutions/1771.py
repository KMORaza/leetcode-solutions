class Solution:
    def longestPalindrome(self, strA: str, strB: str) -> int:
        merged_str = strA + strB
        total_length = len(merged_str)
        max_length = 0
        lps_table = [[0] * total_length for _ in range(total_length)]
        for pos in range(total_length):
            lps_table[pos][pos] = 1
        for gap in range(1, total_length):
            for start_idx in range(total_length - gap):
                end_idx = start_idx + gap
                if merged_str[start_idx] == merged_str[end_idx]:
                    lps_table[start_idx][end_idx] = 2 + lps_table[start_idx + 1][end_idx - 1]
                    if start_idx < len(strA) and end_idx >= len(strA):
                        max_length = max(max_length, lps_table[start_idx][end_idx])
                else:
                    lps_table[start_idx][end_idx] = max(lps_table[start_idx + 1][end_idx], lps_table[start_idx][end_idx - 1])
        return max_length
