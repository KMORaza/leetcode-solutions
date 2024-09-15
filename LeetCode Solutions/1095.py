class Solution:
    def findInMountainArray(self, target: int, mountain_arr) -> int:
        def find_peak(left, right):
            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left
        def binary_search(left, right, target, increasing):
            while left <= right:
                mid = (left + right) // 2
                mid_value = mountain_arr.get(mid)
                if mid_value == target:
                    return mid
                elif (increasing and mid_value < target) or (not increasing and mid_value > target):
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        n = mountain_arr.length()
        if n == 0:
            return -1
        peak = find_peak(0, n - 1)
        result = binary_search(0, peak, target, True)
        if result != -1:
            return result
        return binary_search(peak + 1, n - 1, target, False)
