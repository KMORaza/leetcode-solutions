class NestedInteger:
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = value
    def isInteger(self):
        return self._integer is not None
    def getInteger(self):
        return self._integer
    def getList(self):
        return self._list
class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self._flatten(nestedList)
    def _flatten(self, nestedList):
        self.stack = list(reversed(nestedList))
    def _advance(self):
        while self.stack and not self.stack[-1].isInteger():
            top = self.stack.pop()
            self.stack.extend(reversed(top.getList()))
    def next(self):
        self._advance()
        if self.hasNext():
            return self.stack.pop().getInteger()
        raise Exception("No more elements")
    def hasNext(self):
        self._advance()
        return len(self.stack) > 0