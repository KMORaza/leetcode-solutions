from collections import defaultdict
from math import gcd
class Solution:
    def countPairs(self, values, factor):
        pair_count = 0
        gcd_map = defaultdict(int)
        for value in values:
            current_greatest_common_divisor = gcd(value, factor)
            for stored_gcd in gcd_map.keys():
                if (current_greatest_common_divisor * stored_gcd) % factor == 0:
                    pair_count += gcd_map[stored_gcd]
            gcd_map[current_greatest_common_divisor] += 1
        return pair_count