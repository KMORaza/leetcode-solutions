from math import gcd


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i] > k:
                continue
            if k % nums[i] != 0:
                continue

            current_lcm = nums[i]
            for j in range(i, n):
                if k % nums[j] != 0:
                    break

                current_lcm = current_lcm * nums[j] // gcd(current_lcm, nums[j])

                if current_lcm == k:
                    count += 1
                elif current_lcm > k:
                    break

        return count