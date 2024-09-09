class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
    def _hash(self, key: int) -> int:
        return key % self.size
    def add(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.table[index]
        if key not in bucket:
            bucket.append(key)
    def contains(self, key: int) -> bool:
        index = self._hash(key)
        bucket = self.table[index]
        return key in bucket
    def remove(self, key: int) -> None:
        index = self._hash(key)
        bucket = self.table[index]
        if key in bucket:
            bucket.remove(key)
