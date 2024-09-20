from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_indices = {'type': 0, 'color': 1, 'name': 2}
        index = rule_indices[ruleKey]
        return sum(1 for item in items if item[index] == ruleValue)
