from sortedcontainers import SortedList


class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].remove(index)
            if not self.number_to_indices[old_number]:
                del self.number_to_indices[old_number]

        self.index_to_number[index] = number

        if number not in self.number_to_indices:
            self.number_to_indices[number] = SortedList()
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices:
            return -1
        return self.number_to_indices[number][0]