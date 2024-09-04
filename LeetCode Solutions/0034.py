class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    right = mid - 1
            return -1
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    left = mid + 1
            return -1
        first_pos = find_first(nums, target)
        last_pos = find_last(nums, target)
        return [first_pos, last_pos]
