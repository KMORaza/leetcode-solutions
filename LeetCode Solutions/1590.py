class Solution:
    def minSubarray(self, arr, mod):
        total = sum(arr)
        rem = total % mod
        if rem == 0:
            return 0
        min_length = len(arr)
        prefix_sum = 0
        index_map = {0: -1}
        for idx in range(len(arr)):
            prefix_sum += arr[idx]
            prefix_sum %= mod
            target_prefix = (prefix_sum - rem + mod) % mod
            if target_prefix in index_map:
                min_length = min(min_length, idx - index_map[target_prefix])
            index_map[prefix_sum] = idx
        return min_length if min_length < len(arr) else -1
