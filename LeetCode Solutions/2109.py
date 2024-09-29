from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        space_count = len(spaces)
        for i in range(len(s)):
            if space_index < space_count and i == spaces[space_index]:
                result.append(' ')
                space_index += 1
            result.append(s[i])
        return ''.join(result)

