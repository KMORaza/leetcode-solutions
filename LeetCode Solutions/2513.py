class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        left, right = 1, 2 * 10 ** 9

        while left < right:
            mid = (left + right) // 2

            div1_cnt = mid - mid // divisor1
            div2_cnt = mid - mid // divisor2
            both_excluded = mid - mid // divisor1 - mid // divisor2 + mid // lcm(divisor1, divisor2)

            if (div1_cnt >= uniqueCnt1 and
                    div2_cnt >= uniqueCnt2 and
                    div1_cnt + div2_cnt - both_excluded >= uniqueCnt1 + uniqueCnt2):
                right = mid
            else:
                left = mid + 1

        return left