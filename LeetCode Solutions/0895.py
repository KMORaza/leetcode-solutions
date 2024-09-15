from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFrequency = 0
    def push(self, val: int) -> None:
        freq = self.frequency[val]
        self.frequency[val] += 1
        new_freq = self.frequency[val]
        if new_freq > self.maxFrequency:
            self.maxFrequency = new_freq
        self.group[new_freq].append(val)
    def pop(self) -> int:
        val = self.group[self.maxFrequency].pop()
        self.frequency[val] -= 1
        if not self.group[self.maxFrequency]:
            del self.group[self.maxFrequency]
            self.maxFrequency -= 1
        return val
