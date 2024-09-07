class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target = total_sum // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        n = len(nums)
        used = [False] * n
        def backtrack(index: int, current_sum: int, count: int) -> bool:
            if count == k - 1:
                return True
            if current_sum == target:
                return backtrack(0, 0, count + 1)
            for i in range(index, n):
                if used[i] or current_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i + 1, current_sum + nums[i], count):
                    return True
                used[i] = False
                if current_sum == 0:
                    break
            return False
        return backtrack(0, 0, 0)
