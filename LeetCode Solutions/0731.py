from sortedcontainers import SortedList
class MyCalendarTwo:
    def __init__(self):
        self.bookings = SortedList()
        self.double_bookings = SortedList()
    def book(self, start: int, end: int) -> bool:
        temp_double_bookings = []
        for (d_start, d_end) in self.double_bookings:
            if start < d_end and end > d_start:
                temp_double_bookings.append((max(start, d_start), min(end, d_end)))
        for (b_start, b_end) in temp_double_bookings:
            if b_end > b_start and (start < b_end and end > b_start):
                return False
        for i, (b_start, b_end) in enumerate(self.bookings):
            if start < b_end and end > b_start:
                new_double_start = max(start, b_start)
                new_double_end = min(end, b_end)
                if new_double_end > new_double_start:
                    self.double_bookings.add((new_double_start, new_double_end))
        self.bookings.add((start, end))
        return True
