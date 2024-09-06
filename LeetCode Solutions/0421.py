class Solution:
    def findMaximumXOR(self, nums):
        mask = 0
        max_xor = 0
        prefixes = set()
        for i in range(31, -1, -1):
            mask |= (1 << i)
            current_prefixes = set()
            for num in nums:
                current_prefixes.add(num & mask)
            temp_max_xor = max_xor | (1 << i)
            for prefix in current_prefixes:
                if (prefix ^ temp_max_xor) in current_prefixes:
                    max_xor = temp_max_xor
                    break
        return max_xor
