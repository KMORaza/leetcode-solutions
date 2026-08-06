class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if s == target:
            return True

        s_has_one = '1' in s
        target_has_one = '1' in target

        return s_has_one == target_has_one