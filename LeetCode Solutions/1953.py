from typing import List
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total_milestones = sum(milestones)
        max_milestone = max(milestones)
        if max_milestone > total_milestones - max_milestone:
            return total_milestones - max_milestone
        return total_milestones