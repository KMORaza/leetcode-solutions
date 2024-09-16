import threading
from typing import Callable
class Foo:
    def __init__(self):
        self.event_first = threading.Event()
        self.event_second = threading.Event()
    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.event_first.set()
    def second(self, printSecond: Callable[[], None]) -> None:
        self.event_first.wait()
        printSecond()
        self.event_second.set()
    def third(self, printThird: Callable[[], None]) -> None:
        self.event_second.wait()
        printThird()
