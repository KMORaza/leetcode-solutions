class Solution:
    def findSubarrays(self, arr: List[int]) -> bool:
        seen = set()
        n = len(arr)
        for i in range(n - 1):
            current_sum = arr[i] + arr[i + 1]
            if current_sum in seen:
                return True
            seen.add(current_sum)
        return False