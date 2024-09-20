class Solution:
    def stoneGameVIII(self, arr):
        size = len(arr)
        prefix = [0] * size
        prefix[0] = arr[0]
        for index in range(1, size):
            prefix[index] = prefix[index - 1] + arr[index]
        max_value = prefix[size - 1]
        for index in range(size - 2, 0, -1):
            max_value = max(max_value, prefix[index] - max_value)
        return max_value
