'''
# Memory Limit Exceeded

class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        result = 0

        precompute_left = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            cnt = 0
            val_count = [0] * (n + 1)
            for i in range(j):
                val_count[nums[i]] += 1
            prefix = [0] * (n + 2)
            for v in range(1, n + 1):
                prefix[v + 1] = prefix[v] + val_count[v]
            for threshold in range(n + 1):
                precompute_left[j][threshold] = prefix[threshold]

        right_greater = [[0] * (n + 1) for _ in range(n)]
        for k in range(n):
            cnt = 0
            val_count = [0] * (n + 1)
            for l in range(k + 1, n):
                val_count[nums[l]] += 1
            suffix = [0] * (n + 2)
            for v in range(n, 0, -1):
                suffix[v] = suffix[v + 1] + val_count[v]
            for threshold in range(n + 1):
                right_greater[k][threshold] = suffix[threshold + 1]

        for j in range(n):
            for k in range(j + 1, n):
                if nums[k] < nums[j]:
                    left_cnt = precompute_left[j][nums[k]]
                    right_cnt = right_greater[k][nums[j]]
                    result += left_cnt * right_cnt

        return result
'''

class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        rg = [[0] * (n + 2) for _ in range(n + 1)]
        for k in range(n - 2, -1, -1):
            val = nums[k + 1]
            row_prev = rg[k + 1]
            row_cur = rg[k]
            for v in range(n + 1):
                row_cur[v] = row_prev[v] + (1 if val > v else 0)

        ans = 0
        left_freq = [0] * (n + 2)

        for j in range(1, n - 2):
            left_freq[nums[j - 1]] += 1

            prefix = [0] * (n + 2)
            for v in range(1, n + 1):
                prefix[v] = prefix[v - 1] + left_freq[v]

            nj = nums[j]
            for k in range(j + 1, n - 1):
                nk = nums[k]
                if nj > nk:
                    left_cnt = prefix[nk - 1]
                    right_cnt = rg[k][nj]
                    ans += left_cnt * right_cnt

        return ans