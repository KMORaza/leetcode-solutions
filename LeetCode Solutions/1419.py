class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = [0] * 5
        max_frogs = 0
        for char in croakOfFrogs:
            if char == 'c':
                count[0] += 1
            elif char == 'r':
                if count[0] == 0:
                    return -1
                count[0] -= 1
                count[1] += 1
            elif char == 'o':
                if count[1] == 0:
                    return -1
                count[1] -= 1
                count[2] += 1
            elif char == 'a':
                if count[2] == 0:
                    return -1
                count[2] -= 1
                count[3] += 1
            elif char == 'k':
                if count[3] == 0:
                    return -1
                count[3] -= 1
            else:
                return -1
            max_frogs = max(max_frogs, count[0] + count[1] + count[2] + count[3])
        if any(count):
            return -1
        return max_frogs
