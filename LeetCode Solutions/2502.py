from collections import defaultdict
import bisect


class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.free = [(0, n)]
        self.alloc = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for i, (start, length) in enumerate(self.free):
            if length >= size:
                new_start = start
                remaining = length - size

                if remaining == 0:
                    self.free.pop(i)
                else:
                    self.free[i] = (start + size, remaining)

                self.alloc[mID].append((new_start, size))
                return new_start

        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self.alloc:
            return 0

        blocks = self.alloc.pop(mID)
        total_freed = sum(length for _, length in blocks)

        for start, length in blocks:
            self._add_free_block(start, length)

        return total_freed

    def _add_free_block(self, start: int, length: int):
        pos = bisect.bisect_left(self.free, (start,))

        if pos < len(self.free):
            r_start, r_len = self.free[pos]
            if start + length == r_start:
                length += r_len
                self.free.pop(pos)

        if pos > 0:
            l_start, l_len = self.free[pos - 1]
            if l_start + l_len == start:
                start = l_start
                length += l_len
                self.free.pop(pos - 1)
                pos -= 1

        self.free.insert(pos, (start, length))