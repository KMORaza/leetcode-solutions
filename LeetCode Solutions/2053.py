from collections import Counter
from typing import List
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct_strings = [s for s in arr if count[s] == 1]
        return distinct_strings[k - 1] if k <= len(distinct_strings) else ""
