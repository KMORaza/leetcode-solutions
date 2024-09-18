class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            if len(self.stack) > 1:
                self.inc[len(self.stack) - 2] += 0
    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]
        res = self.stack.pop() + self.inc[idx]
        self.inc[idx] = 0
        return res
    def increment(self, k: int, val: int) -> None:
        if self.stack:
            idx = min(k, len(self.stack)) - 1
            self.inc[idx] += val
