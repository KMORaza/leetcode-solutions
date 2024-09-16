import threading
from typing import Callable
class ZeroEvenOdd:
    def __init__(self, n: int):
        self.n = n
        self.zero_event = threading.Event()
        self.even_event = threading.Event()
        self.odd_event = threading.Event()
        self.zero_event.set()
        self.even_event.clear()
        self.odd_event.clear()
        self.current = 1
    def zero(self, printNumber: Callable[[int], None]) -> None:
        for _ in range(self.n):
            self.zero_event.wait()
            printNumber(0)
            if self.current % 2 == 0:
                self.even_event.set()
            else:
                self.odd_event.set()
            self.zero_event.clear()
    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(2, self.n + 1, 2):
            self.even_event.wait()
            printNumber(i)
            self.current += 1
            self.zero_event.set()
            self.even_event.clear()
    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_event.wait()
            printNumber(i)
            self.current += 1
            self.zero_event.set()
            self.odd_event.clear()
