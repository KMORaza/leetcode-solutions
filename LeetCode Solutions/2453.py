class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        from collections import Counter

        mod_count = Counter()
        for num in nums:
            mod_count[num % space] += 1

        max_count = max(mod_count.values())
        result = float('inf')

        for num in nums:
            if mod_count[num % space] == max_count:
                result = min(result, num)

        return result