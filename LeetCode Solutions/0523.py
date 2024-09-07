class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        mod_map = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            current_mod = prefix_sum % k
            if current_mod in mod_map:
                if i - mod_map[current_mod] > 1:
                    return True
            else:
                mod_map[current_mod] = i
        return False
