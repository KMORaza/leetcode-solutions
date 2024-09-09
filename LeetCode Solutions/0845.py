class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        max_length = 0
        for i in range(1, n - 1):
            if A[i - 1] < A[i] > A[i + 1]:
                left = i - 1
                right = i + 1
                while left > 0 and A[left - 1] < A[left]:
                    left -= 1
                while right < n - 1 and A[right + 1] < A[right]:
                    right += 1
                current_length = right - left + 1
                max_length = max(max_length, current_length)
        return max_length
