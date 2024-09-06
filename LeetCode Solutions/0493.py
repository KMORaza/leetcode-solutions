class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_count_split_inv(nums, temp, left, mid, right):
            j = mid + 1
            count = 0
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            i, j, k = left, mid + 1, left
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
            for i in range(left, right + 1):
                nums[i] = temp[i]
            return count
        def merge_sort(nums, temp, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(nums, temp, left, mid)
            count += merge_sort(nums, temp, mid + 1, right)
            count += merge_count_split_inv(nums, temp, left, mid, right)
            return count
        temp = [0] * len(nums)
        return merge_sort(nums, temp, 0, len(nums) - 1)
