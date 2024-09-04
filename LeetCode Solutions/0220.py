from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        sorted_list = SortedList()
        for i, num in enumerate(nums):
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            pos = sorted_list.bisect_left(num)
            if pos < len(sorted_list) and sorted_list[pos] <= num + valueDiff:
                return True
            if pos > 0 and sorted_list[pos - 1] >= num - valueDiff:
                return True
            sorted_list.add(num)
        return False