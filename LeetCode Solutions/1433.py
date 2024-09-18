class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        def canBreak(s1_sorted, s2_sorted):
            for ch1, ch2 in zip(s1_sorted, s2_sorted):
                if ch1 < ch2:
                    return False
            return True
        return canBreak(s1_sorted, s2_sorted) or canBreak(s2_sorted, s1_sorted)
