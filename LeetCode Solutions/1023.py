from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self._matches(query, pattern) for query in queries]
    def _matches(self, text: str, pattern: str) -> bool:
        pattern_index = 0
        for char in text:
            if pattern_index < len(pattern) and char == pattern[pattern_index]:
                pattern_index += 1
            elif char.isupper():
                return False
        return pattern_index == len(pattern)
