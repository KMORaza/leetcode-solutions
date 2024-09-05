class PeekingIterator:
    def __init__(self, iterator):
        self._iterator = iterator
        self._next_element = None
        self._has_next = False
        self._advance()
    def _advance(self):
        if self._iterator.hasNext():
            self._next_element = self._iterator.next()
            self._has_next = True
        else:
            self._has_next = False
            self._next_element = None
    def peek(self):
        return self._next_element
    def next(self):
        if not self._has_next:
            raise Exception("No more elements")
        current = self._next_element
        self._advance()
        return current
    def hasNext(self):
        return self._has_next
