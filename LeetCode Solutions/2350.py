class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        res = 1
        for roll in rolls:
            seen.add(roll)
            if len(seen) == k:
                res += 1
                seen.clear()
        return res