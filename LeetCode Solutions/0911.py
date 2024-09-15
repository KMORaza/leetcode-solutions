from bisect import bisect_right
from collections import defaultdict
from typing import List
class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        vote_count = defaultdict(int)
        current_leader = -1
        max_votes = 0
        for person, time in zip(persons, times):
            vote_count[person] += 1
            if vote_count[person] >= max_votes:
                if vote_count[person] > max_votes or current_leader != person:
                    current_leader = person
                    max_votes = vote_count[person]
            self.leaders.append(current_leader)
    def q(self, t: int) -> int:
        index = bisect_right(self.times, t) - 1
        return self.leaders[index]
