from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)
        players = set()
        for winner, loser in matches:
            loss_count[loser] += 1
            players.add(winner)
            players.add(loser)
        no_loss = []
        one_loss = []
        for player in players:
            if loss_count[player] == 0:
                no_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
        return [sorted(no_loss), sorted(one_loss)]