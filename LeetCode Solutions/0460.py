from collections import defaultdict, OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0
    def _update_freq(self, key: int):
        freq = self.key_to_freq[key]
        self.freq_to_keys[freq].pop(key)
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.key_to_freq[key] += 1
        new_freq = self.key_to_freq[key]
        self.freq_to_keys[new_freq][key] = None
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = OrderedDict()
        self.freq_to_keys[new_freq][key] = None
    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1
        self._update_freq(key)
        return self.key_to_value[key]
    def put(self, key: int, value: int):
        if self.capacity <= 0:
            return
        if key in self.key_to_value:
            self.key_to_value[key] = value
            self._update_freq(key)
        else:
            if len(self.key_to_value) >= self.capacity:
                lfu_keys = self.freq_to_keys[self.min_freq]
                oldest_key, _ = lfu_keys.popitem(last=False)
                del self.key_to_value[oldest_key]
                del self.key_to_freq[oldest_key]
                if not lfu_keys:
                    del self.freq_to_keys[self.min_freq]
            self.key_to_value[key] = value
            self.key_to_freq[key] = 1
            self.min_freq = 1
            self.freq_to_keys[1][key] = None
