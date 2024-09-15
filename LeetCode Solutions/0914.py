from typing import List
from collections import Counter
from math import gcd
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        frequencies = count.values()
        overall_gcd = reduce(gcd, frequencies)
        return overall_gcd >= 2
