from collections import deque
class BinaryIndexedTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    def update(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += self._lowbit(index)
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= self._lowbit(index)
        return total
    @staticmethod
    def _lowbit(index):
        return index & -index
class Solution:
    def minInteger(self, num: str, x: int) -> str:
        length = len(num)
        result = []
        bit = BinaryIndexedTree(length)
        marked = [False] * length
        digit_positions = [deque() for _ in range(10)]
        for pos, char in enumerate(num):
            digit_positions[int(char)].append(pos)
        while x > 0 and len(result) < length:
            for digit in range(10):
                if not digit_positions[digit]:
                    continue
                position = digit_positions[digit][0]
                cost = position - bit.query(position + 1)
                if cost > x:
                    continue
                x -= cost
                result.append(str(digit))
                marked[position] = True
                bit.update(position + 1, 1)
                digit_positions[digit].popleft()
                break
        for pos in range(length):
            if not marked[pos]:
                result.append(num[pos])
        return ''.join(result)
