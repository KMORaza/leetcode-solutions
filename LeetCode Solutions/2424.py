class LUPrefix:
    def __init__(self, n: int):
        self.n = n
        self.uploaded = [False] * (n + 1)
        self.longest_prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.longest_prefix + 1 <= self.n and self.uploaded[self.longest_prefix + 1]:
            self.longest_prefix += 1

    def longest(self) -> int:
        return self.longest_prefix