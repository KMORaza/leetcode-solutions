import random
class RandomizedCollection:
    def __init__(self):
        self.val_to_indices = {}
        self.values = []
    def insert(self, val: int) -> bool:
        if val not in self.val_to_indices:
            self.val_to_indices[val] = set()
        self.val_to_indices[val].add(len(self.values))
        self.values.append(val)
        return len(self.val_to_indices[val]) == 1
    def remove(self, val: int) -> bool:
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False
        remove_index = self.val_to_indices[val].pop()
        last_val = self.values[-1]
        self.values[remove_index] = last_val
        if self.val_to_indices[last_val]:
            self.val_to_indices[last_val].add(remove_index)
            self.val_to_indices[last_val].remove(len(self.values) - 1)
        self.values.pop()
        if not self.val_to_indices[val]:
            del self.val_to_indices[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.values)
