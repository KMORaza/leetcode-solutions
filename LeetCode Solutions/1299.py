class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [-1] * n
        max_from_right = -1
        for i in range(n - 1, -1, -1):
            result[i] = max_from_right
            if arr[i] > max_from_right:
                max_from_right = arr[i]
        return result
