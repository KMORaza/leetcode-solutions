from typing import List
from collections import Counter
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_count = Counter(answers)
        min_rabbits = 0
        for answer, count in answer_count.items():
            groups = math.ceil(count / (answer + 1))
            min_rabbits += groups * (answer + 1)
        return min_rabbits
