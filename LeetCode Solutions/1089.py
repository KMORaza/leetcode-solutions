class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        zeros = 0
        for i in range(n):
            if arr[i] == 0:
                zeros += 1
        i = n - 1
        j = n + zeros - 1
        while i >= 0:
            if arr[i] == 0:
                if j < n:
                    arr[j] = 0
                j -= 1
                if j < n:
                    arr[j] = 0
                j -= 1
            else:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
            i -= 1
