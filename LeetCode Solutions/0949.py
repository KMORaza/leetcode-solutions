from itertools import permutations
from typing import List
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def is_valid_time(h, m):
            return 0 <= h < 24 and 0 <= m < 60
        max_time = -1
        for perm in permutations(arr):
            h, m = perm[0] * 10 + perm[1], perm[2] * 10 + perm[3]
            if is_valid_time(h, m):
                max_time = max(max_time, h * 60 + m)
        if max_time == -1:
            return ""
        h, m = divmod(max_time, 60)
        return f"{h:02}:{m:02}"
