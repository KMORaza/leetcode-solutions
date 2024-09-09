import random
class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        self.n = n
        self.blacklist = set(blacklist)
        self.size = n - len(blacklist)
        self.map = {}
        blacklist.sort()
        last_valid = self.size
        for bl in blacklist:
            if bl < last_valid:
                while last_valid in self.blacklist:
                    last_valid += 1
                self.map[bl] = last_valid
                last_valid += 1
    def pick(self) -> int:
        rand_index = random.randint(0, self.size - 1)
        return self.map.get(rand_index, rand_index)
