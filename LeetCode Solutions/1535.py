from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        current_winner = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                current_winner = arr[i]
                count = 1
            else:
                count += 1
            if count == k:
                return current_winner
        return current_winner
