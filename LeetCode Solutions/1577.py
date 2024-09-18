from collections import defaultdict
from typing import List
class Solution:
    def numTriplets(self, array1: List[int], array2: List[int]) -> int:
        return self._countTriplets(array1, array2) + self._countTriplets(array2, array1)
    def _countTriplets(self, firstArray: List[int], secondArray: List[int]) -> int:
        total = 0
        frequency = defaultdict(int)
        for value in secondArray:
            frequency[value] += 1
        for item in firstArray:
            targetValue = item * item
            for key, freq in frequency.items():
                if targetValue % key > 0:
                    continue
                complementaryValue = targetValue // key
                if complementaryValue in frequency:
                    if complementaryValue == key:
                        total += freq * (freq - 1)
                    else:
                        total += freq * frequency[complementaryValue]
        return total // 2