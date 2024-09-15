class RLEIterator:
    def __init__(self, sequence):
        self.encoding = sequence
        self.pointer = 0
        self.offset = 0
    def next(self, k):
        while self.pointer < len(self.encoding):
            if self.offset + k > self.encoding[self.pointer]:
                k -= self.encoding[self.pointer] - self.offset
                self.pointer += 2
                self.offset = 0
            else:
                self.offset += k
                return self.encoding[self.pointer + 1]
        return -1
