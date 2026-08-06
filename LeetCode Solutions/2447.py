class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] % k != 0:
                continue

            current_gcd = nums[i]
            for j in range(i, n):
                if nums[j] % k != 0:
                    break

                current_gcd = self.gcd(current_gcd, nums[j])
                if current_gcd == k:
                    count += 1
                elif current_gcd < k:
                    break

        return count

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a