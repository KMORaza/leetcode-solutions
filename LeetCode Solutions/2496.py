class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = 0

        for s in strs:
            try:
                val = int(s)
            except ValueError:
                val = len(s)
            max_val = max(max_val, val)

        return max_val