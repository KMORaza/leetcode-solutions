class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            smallest = s
            for i in range(1, len(s)):
                rotated = s[i:] + s[:i]
                if rotated < smallest:
                    smallest = rotated
            return smallest
        else:
            return ''.join(sorted(s))
