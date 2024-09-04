from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))
        largest_num = ''.join(nums_str)
        if largest_num[0] == '0':
            return '0'
        return largest_num