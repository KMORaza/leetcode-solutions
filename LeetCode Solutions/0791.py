from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []

        for char in order:
            if char in count:
                result.append(char * count[char])
                del count[char]
        for char in count:
            result.append(char * count[char])
        return ''.join(result)
