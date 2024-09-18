from typing import List
class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * (n + 1)
        self.pointer = 1
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        result = []
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            result.append(self.stream[self.pointer])
            self.pointer += 1
        return result
