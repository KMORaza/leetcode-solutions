import re
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = re.findall(r'\d+', word)
        unique_integers = set(int(num) for num in numbers)
        return len(unique_integers)
