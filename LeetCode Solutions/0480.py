from sortedcontainers import SortedList
import bisect
class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        sorted_window = SortedList()
        result = []
        def get_median():
            if k % 2 == 1:
                return float(sorted_window[k // 2])
            else:
                return (sorted_window[k // 2 - 1] + sorted_window[k // 2]) / 2
        for i in range(len(nums)):
            num = nums[i]
            sorted_window.add(num)
            if i >= k:
                sorted_window.remove(nums[i - k])
            if i >= k - 1:
                result.append(get_median())
        return result
