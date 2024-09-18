from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def can_make_bouquets(day: int) -> bool:
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                else:
                    flowers = 0
                if flowers >= k:
                    bouquets += 1
                    flowers = 0
                if bouquets >= m:
                    return True
            return bouquets >= m
        if m * k > len(bloomDay):
            return -1
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if can_make_bouquets(mid):
                right = mid
            else:
                left = mid + 1
        return left
