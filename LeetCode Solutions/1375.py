class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        bulbs = [0] * len(flips)
        max_flipped = 0
        count = 0
        for i, flip in enumerate(flips):
            bulbs[flip - 1] = 1
            max_flipped = max(max_flipped, flip)
            if max_flipped == i + 1:
                count += 1
        return count
