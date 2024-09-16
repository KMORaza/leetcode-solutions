from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        freq = Counter(nums)
        unique_nums = sorted(freq.keys())
        for num in unique_nums:
            if freq[num] > 0:
                count = freq[num]
                for i in range(k):
                    if freq[num + i] < count:
                        return False
                    freq[num + i] -= count
        return True
