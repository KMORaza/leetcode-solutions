class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x: int) -> int:
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x //= 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps
        numbers = [(power(i), i) for i in range(lo, hi + 1)]
        numbers.sort()
        return numbers[k - 1][1]
