from typing import List
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        total_days = len(security)
        valid_days = []
        drop_streak = [0] * total_days
        rise_streak = [0] * total_days
        for current_day in range(1, total_days):
            if security[current_day - 1] >= security[current_day]:
                drop_streak[current_day] = drop_streak[current_day - 1] + 1
        for current_day in range(total_days - 2, -1, -1):
            if security[current_day] <= security[current_day + 1]:
                rise_streak[current_day] = rise_streak[current_day + 1] + 1
        for current_day in range(total_days):
            if drop_streak[current_day] >= time and rise_streak[current_day] >= time:
                valid_days.append(current_day)
        return valid_days