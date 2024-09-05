class Solution:
    def wiggleSort(self, nums):
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        left = nums[:mid]
        right = nums[mid:]
        left.reverse()
        right.reverse()
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            result.append(left[i])
            result.append(right[j])
            i += 1
            j += 1
        if i < len(left):
            result.extend(left[i:])
        if j < len(right):
            result.extend(right[j:])
        for k in range(n):
            nums[k] = result[k]
