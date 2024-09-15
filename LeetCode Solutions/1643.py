from math import comb
from typing import List
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        d, h = destination
        path = []
        while d > 0 or h > 0:
            if d == 0:
                path.append('H')
                h -= 1
            elif h == 0:
                path.append('V')
                d -= 1
            else:
                paths_with_H = comb(d + h - 1, d)
                if k <= paths_with_H:
                    path.append('H')
                    h -= 1
                else:
                    path.append('V')
                    k -= paths_with_H
                    d -= 1
        return ''.join(path)
