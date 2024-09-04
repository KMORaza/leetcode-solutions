class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                low = mid + 1
            else:
                high = mid - 1
        return high
