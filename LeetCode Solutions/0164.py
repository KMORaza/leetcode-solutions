class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        buckets = [[None, None] for _ in range(bucket_count)]
        for num in nums:
            idx = (num - min_val) // bucket_size
            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        max_gap = 0
        prev_max = buckets[0][1]
        for i in range(1, bucket_count):
            if buckets[i][0] is not None:
                max_gap = max(max_gap, buckets[i][0] - prev_max)
                prev_max = buckets[i][1]
        return max_gap
