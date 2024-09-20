from sortedcontainers import SortedList
class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.elements = []
        self.sorted_elements = SortedList()
        self.valid_elements = 0
    def addElement(self, num: int) -> None:
        if self.valid_elements < self.m:
            self.elements.append(num)
            self.sorted_elements.add(num)
            self.valid_elements += 1
        else:
            oldest = self.elements.pop(0)
            self.sorted_elements.remove(oldest)
            self.elements.append(num)
            self.sorted_elements.add(num)
    def calculateMKAverage(self) -> int:
        if self.valid_elements < self.m:
            return -1
        total = sum(self.sorted_elements[self.k:self.m - self.k])
        return total // (self.m - 2 * self.k)
