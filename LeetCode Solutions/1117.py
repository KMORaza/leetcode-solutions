import threading
class H2O:
    def __init__(self):
        self.h_count = 0
        self.o_count = 0
        self.lock = threading.Lock()
        self.h_cond = threading.Condition(self.lock)
        self.o_cond = threading.Condition(self.lock)
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.lock:
            while self.h_count == 2:
                self.h_cond.wait()
            releaseHydrogen()
            self.h_count += 1
            if self.h_count == 2 and self.o_count == 1:
                self.h_count = 0
                self.o_count = 0
                self.h_cond.notify_all()
                self.o_cond.notify_all()
            else:
                self.o_cond.notify()
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.lock:
            while self.h_count < 2:
                self.o_cond.wait()
            releaseOxygen()
            self.h_count = 0
            self.o_count = 0
            self.h_cond.notify_all()
            self.o_cond.notify_all()
