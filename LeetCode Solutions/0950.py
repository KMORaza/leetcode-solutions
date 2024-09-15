from collections import deque
from typing import List
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        result = deque()
        for card in reversed(sorted_deck):
            if result:
                result.appendleft(result.pop())
            result.appendleft(card)
        return list(result)
