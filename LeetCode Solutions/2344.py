class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        overall_gcd = numsDivide[0]
        for x in numsDivide[1:]:
            overall_gcd = gcd(overall_gcd, x)

        nums.sort()

        for i, num in enumerate(nums):
            if overall_gcd % num == 0:
                return i
            if num > overall_gcd:
                break

        return -1