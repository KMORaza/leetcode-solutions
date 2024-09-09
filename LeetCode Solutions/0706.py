class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size
    def _hash(self, key: int) -> int:
        return key % self.size
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = ListNode(key, value)
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)
    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1
    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.table[index]
        if current is None:
            return
        if current.key == key:
            self.table[index] = current.next
        else:
            prev = current
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next
