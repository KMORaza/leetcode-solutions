from typing import List
class Solution:
    def maximumEvenSplit(self, total: int) -> List[int]:
        if total % 2 == 1:
            return []
        even_numbers = []
        remainder = total
        next_even = 2
        while remainder - next_even >= next_even + 2:
            even_numbers.append(next_even)
            remainder -= next_even
            next_even += 2
        even_numbers.append(remainder)
        return even_numbers