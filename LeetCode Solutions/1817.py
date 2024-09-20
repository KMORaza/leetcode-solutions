from typing import List
from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, userLogs: List[List[int]], totalMinutes: int) -> List[int]:
        userActivity = defaultdict(set)
        for userId, minute in userLogs:
            userActivity[userId].add(minute)
        activityCount = [0] * totalMinutes
        for minutes in userActivity.values():
            activityCount[len(minutes) - 1] += 1
        return activityCount
