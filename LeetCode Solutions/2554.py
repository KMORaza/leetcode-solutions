class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        current_sum = 0
        count = 0

        for i in range(1, n + 1):
            if i in banned_set:
                continue
            if current_sum + i > maxSum:
                break
            current_sum += i
            count += 1

        return count