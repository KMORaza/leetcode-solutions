class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        def check_valid_base(base: int, m: int) -> bool:
            return base ** m - 1 == n * (base - 1)
        import math
        def find_base_for_m(m: int) -> int:
            low, high = 2, int(n**0.5) + 1
            while low <= high:
                mid = (low + high) // 2
                if check_valid_base(mid, m):
                    return mid
                elif mid ** m > n * (mid - 1) + 1:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        max_m = int(math.log2(n)) + 1
        for m in range(max_m, 1, -1):
            base = find_base_for_m(m)
            if base != -1:
                return str(base)
        return str(n - 1)