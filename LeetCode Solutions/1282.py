from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for person_id, group_size in enumerate(groupSizes):
            if group_size not in groups:
                groups[group_size] = []
            groups[group_size].append(person_id)
            if len(groups[group_size]) == group_size:
                result.append(groups[group_size])
                groups[group_size] = []
        return result
