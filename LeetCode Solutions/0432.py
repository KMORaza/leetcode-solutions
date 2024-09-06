from collections import defaultdict
from sortedcontainers import SortedDict
class AllOne:
    def __init__(self):
        self.count_map = {}
        self.freq_map = defaultdict(set)
        self.counts = SortedDict()
    def inc(self, key: str) -> None:
        if key in self.count_map:
            old_count = self.count_map[key]
            new_count = old_count + 1
            self.count_map[key] = new_count
            self.freq_map[old_count].remove(key)
            if not self.freq_map[old_count]:
                del self.freq_map[old_count]
                self.counts.pop(old_count, None)
            if new_count in self.freq_map:
                self.freq_map[new_count].add(key)
            else:
                self.freq_map[new_count] = {key}
            self.counts[new_count] = self.counts.get(new_count, 0) + 1
        else:
            self.count_map[key] = 1
            self.freq_map[1].add(key)
            self.counts[1] = self.counts.get(1, 0) + 1
    def dec(self, key: str) -> None:
        old_count = self.count_map[key]
        if old_count == 1:
            del self.count_map[key]
            self.freq_map[old_count].remove(key)
            if not self.freq_map[old_count]:
                del self.freq_map[old_count]
                self.counts.pop(old_count, None)
        else:
            new_count = old_count - 1
            self.count_map[key] = new_count
            self.freq_map[old_count].remove(key)
            if not self.freq_map[old_count]:
                del self.freq_map[old_count]
                self.counts.pop(old_count, None)
            if new_count in self.freq_map:
                self.freq_map[new_count].add(key)
            else:
                self.freq_map[new_count] = {key}
            self.counts[new_count] = self.counts.get(new_count, 0) + 1
    def getMaxKey(self) -> str:
        if not self.counts:
            return ""
        return next(iter(self.freq_map[self.counts.peekitem(-1)[0]]))
    def getMinKey(self) -> str:
        if not self.counts:
            return ""
        return next(iter(self.freq_map[self.counts.peekitem(0)[0]]))
