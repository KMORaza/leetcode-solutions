class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diff = [(i, sc, gc) for i, (sc, gc) in enumerate(zip(s, goal)) if sc != gc]
        if len(diff) != 2:
            return False
        (i1, sc1, gc1), (i2, sc2, gc2) = diff
        return sc1 == gc2 and sc2 == gc1
