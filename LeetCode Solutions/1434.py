from typing import List
from collections import defaultdict
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        x = 1000000007
        N = len(hats)
        hat_to_people = defaultdict(list)
        for person, hats_list in enumerate(hats):
            for hat in hats_list:
                hat_to_people[hat].append(person)
        dp = [0] * (1 << N)
        dp[0] = 1
        for hat in range(1, 41):
            if hat not in hat_to_people:
                continue
            people = hat_to_people[hat]
            for mask in range((1 << N) - 1, -1, -1):
                if dp[mask] == 0:
                    continue
                for person in people:
                    if mask & (1 << person) == 0:
                        new_mask = mask | (1 << person)
                        dp[new_mask] = (dp[new_mask] + dp[mask]) % x
        return dp[(1 << N) - 1]
