from collections import deque
class FrontMiddleBackQueue:
    def __init__(self):
        self.front = deque()
        self.back = deque()
    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()
    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
            self.front.append(val)
        else:
            self.front.append(val)
        self._balance()
    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()
    def popFront(self) -> int:
        if not self.front and not self.back:
            return -1
        if self.front:
            val = self.front.popleft()
        else:
            val = self.back.popleft()
        self._balance()
        return val
    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) > len(self.back):
            val = self.front.pop()
        else:
            val = self.front.pop() if self.front else self.back.popleft()
        self._balance()
        return val
    def popBack(self) -> int:
        if not self.back and not self.front:
            return -1
        if self.back:
            val = self.back.pop()
        else:
            val = self.front.pop()
        self._balance()
        return val
    def _balance(self):
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.back) > len(self.front):
            self.front.append(self.back.popleft())
