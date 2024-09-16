from math import gcd
def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def countUglyNumbers(x: int) -> int:
            count = (x // a) + (x // b) + (x // c)
            count -= (x // lcm(a, b)) + (x // lcm(b, c)) + (x // lcm(a, c))
            count += (x // lcm(a, lcm(b, c)))
            return count
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if countUglyNumbers(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left