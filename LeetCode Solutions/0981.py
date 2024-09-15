from typing import List, Tuple
from collections import defaultdict
import bisect
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        i = bisect.bisect_right(values, (timestamp, chr(255)))
        if i == 0:
            return ""
        return values[i - 1][1]
