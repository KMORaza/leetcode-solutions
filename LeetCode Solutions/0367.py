class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        low, high = 1, num
        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid
            if mid_squared == num:
                return True
            elif mid_squared < num:
                low = mid + 1
            else:
                high = mid - 1
        return False