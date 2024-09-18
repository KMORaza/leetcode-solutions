from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        count = Counter(s)
        result = []
        while count:
            for char in sorted(count.keys()):
                result.append(char)
                count[char] -= 1
                if count[char] == 0:
                    del count[char]
            for char in sorted(count.keys(), reverse=True):
                result.append(char)
                count[char] -= 1
                if count[char] == 0:
                    del count[char]
        return ''.join(result)
