from typing import List
class Solution:
    def canFormSubsequence(self, s: str, p: str, removable: List[int], k: int) -> bool:
        removed_set = set(removable[:k])
        j = 0
        for i in range(len(s)):
            if i in removed_set:
                continue
            if j < len(p) and s[i] == p[j]:
                j += 1
        return j == len(p)
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        left, right = 0, len(removable)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if self.canFormSubsequence(s, p, removable, mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer
