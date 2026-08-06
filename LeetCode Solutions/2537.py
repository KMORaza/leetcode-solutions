class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}
        good_pairs = 0
        result = 0
        left = 0

        for right in range(n):
            num = nums[right]
            if num in count:
                good_pairs -= count[num] * (count[num] - 1) // 2

            count[num] = count.get(num, 0) + 1

            good_pairs += count[num] * (count[num] - 1) // 2

            while good_pairs >= k:
                result += n - right
                left_num = nums[left]

                good_pairs -= count[left_num] * (count[left_num] - 1) // 2
                count[left_num] -= 1
                if count[left_num] == 0:
                    del count[left_num]
                else:
                    good_pairs += count[left_num] * (count[left_num] - 1) // 2

                left += 1

        return result