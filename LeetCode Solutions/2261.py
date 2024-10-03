from typing import List
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        distinct_subarrays = set()
        n = len(nums)
        for start in range(n):
            count = 0
            subarray = []
            for end in range(start, n):
                subarray.append(nums[end])
                if nums[end] % p == 0:
                    count += 1
                if count > k:
                    break
                distinct_subarrays.add(tuple(subarray))
        return len(distinct_subarrays)
