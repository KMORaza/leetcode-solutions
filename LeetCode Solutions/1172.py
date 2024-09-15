from collections import deque
from sortedcontainers import SortedSet
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.not_full = SortedSet()
    def push(self, output: int) -> None:
        if not self.not_full:
            new_stack = deque([output])
            self.stacks.append(new_stack)
            if self.capacity > 1:
                self.not_full.add(len(self.stacks) - 1)
        else:
            index = self.not_full[0]
            self.stacks[index].append(output)
            if len(self.stacks[index]) == self.capacity:
                self.not_full.discard(index)
    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)
    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        output = self.stacks[index].pop()
        if index == len(self.stacks) - 1 and not self.stacks[index]:
            while self.stacks and not self.stacks[-1]:
                self.not_full.discard(len(self.stacks) - 1)
                self.stacks.pop()
        else:
            self.not_full.add(index)
        return output
