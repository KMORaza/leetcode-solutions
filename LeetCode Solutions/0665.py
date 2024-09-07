class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        index = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                index = i
                if count > 1:
                    return False
        if count == 0:
            return True
        if index == 0 or nums[index - 1] <= nums[index + 1]:
            return True
        if index + 1 == n - 1 or nums[index] <= nums[index + 2]:
            return True
        return False
