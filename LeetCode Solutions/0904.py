from typing import List
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_length = 0
        fruit_count = defaultdict(int)
        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
