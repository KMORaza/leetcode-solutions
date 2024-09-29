from itertools import permutations
from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        even_numbers = set()
        for perm in permutations(digits, 3):
            if perm[2] % 2 == 0 and perm[0] != 0:
                number = int(''.join(map(str, perm)))
                even_numbers.add(number)
        return sorted(even_numbers)