from typing import List
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        index_map = {}
        min_pickup = float('inf')
        for i, card in enumerate(cards):
            if card in index_map:
                min_pickup = min(min_pickup, i - index_map[card] + 1)
            index_map[card] = i
        return min_pickup if min_pickup != float('inf') else -1
