class Solution:
    def captureForts(self, forts: List[int]) -> int:
        max_captured = 0
        i = 0
        n = len(forts)

        while i < n:
            if forts[i] == 1:
                j = i + 1
                while j < n and forts[j] == 0:
                    j += 1
                if j < n and forts[j] == -1:
                    max_captured = max(max_captured, j - i - 1)
                i = j
            elif forts[i] == -1:
                j = i + 1
                while j < n and forts[j] == 0:
                    j += 1
                if j < n and forts[j] == 1:
                    max_captured = max(max_captured, j - i - 1)
                i = j
            else:
                i += 1

        return max_captured