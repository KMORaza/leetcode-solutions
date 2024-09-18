from collections import defaultdict
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        count = defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for i, team in enumerate(vote):
                count[team][i] += 1
        sorted_teams = sorted(count.keys(), key=lambda team: (count[team], -ord(team)), reverse=True)
        return ''.join(sorted_teams)
