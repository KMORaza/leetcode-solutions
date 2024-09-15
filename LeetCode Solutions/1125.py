from itertools import combinations
from collections import defaultdict
class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)
        person_mask = []
        for person in people:
            mask = 0
            for skill in person:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            person_mask.append(mask)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        team = [0] * (1 << n)
        for mask in range(1 << n):
            for i, p_mask in enumerate(person_mask):
                new_mask = mask | p_mask
                if dp[new_mask] > dp[mask] + 1:
                    dp[new_mask] = dp[mask] + 1
                    team[new_mask] = team[mask] | (1 << i)
        result = []
        final_mask = (1 << n) - 1
        mask = team[final_mask]
        for i in range(len(people)):
            if mask & (1 << i):
                result.append(i)
        return result

