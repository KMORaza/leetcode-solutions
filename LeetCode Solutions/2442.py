class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_nums = set(nums)

        for num in nums:
            reversed_num = int(str(num)[::-1])
            distinct_nums.add(reversed_num)

        return len(distinct_nums)