class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.count_ones = 0
    def fix(self, idx: int) -> None:
        if not self.flipped:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.count_ones += 1
        else:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.count_ones += 1
    def unfix(self, idx: int) -> None:
        if not self.flipped:
            if self.bits[idx] == 1:
                self.bits[idx] = 0
                self.count_ones -= 1
        else:
            if self.bits[idx] == 0:
                self.bits[idx] = 1
                self.count_ones -= 1
    def flip(self) -> None:
        self.flipped = not self.flipped
        self.count_ones = self.size - self.count_ones
    def all(self) -> bool:
        return self.count_ones == self.size
    def one(self) -> bool:
        return self.count_ones > 0
    def count(self) -> int:
        return self.count_ones
    def toString(self) -> str:
        if self.flipped:
            return ''.join('0' if bit == 1 else '1' for bit in self.bits)
        return ''.join(str(bit) for bit in self.bits)
