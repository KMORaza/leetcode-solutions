class Solution:
    def trailing_zeroes_count(self, x: int) -> int:
        count = 0
        while x > 0:
            x //= 5
            count += x
        return count
    def find_first_with_k_zeroes(self, k: int) -> int:
        low, high = 0, 5 * (k + 1)
        while low < high:
            mid = (low + high) // 2
            if self.trailing_zeroes_count(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low if self.trailing_zeroes_count(low) == k else -1
    def find_first_with_more_than_k_zeroes(self, k: int) -> int:
        low, high = 0, 5 * (k + 1)
        while low < high:
            mid = (low + high) // 2
            if self.trailing_zeroes_count(mid) <= k:
                low = mid + 1
            else:
                high = mid
        return low
    def preimageSizeFZF(self, k: int) -> int:
        if k == 0:
            return 5
        start = self.find_first_with_k_zeroes(k)
        if start == -1:
            return 0
        end = self.find_first_with_more_than_k_zeroes(k)
        return end - start
