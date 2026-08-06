class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        even_nums = [num for num in nums if num % 2 == 0]
        if not even_nums:
            return -1

        count = Counter(even_nums)
        max_freq = max(count.values())
        result = float('inf')

        for num, freq in count.items():
            if freq == max_freq:
                result = min(result, num)

        return result