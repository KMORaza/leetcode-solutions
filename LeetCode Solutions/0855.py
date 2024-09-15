class NodeClass:
    def __init__(self, value):
        self.previous = None
        self.next_node = None
        self.value = value
class ExamRoom:
    def __init__(self, n: int):
        self.total_seats = n
        self.start = NodeClass(-1)
        self.end = NodeClass(-1)
        self.start.next_node = self.end
        self.end.previous = self.start
        self.position_map = {}
    def seat(self) -> int:
        if self.start.next_node == self.end:
            new_node = NodeClass(0)
            self._connect(self.start, new_node)
            self._connect(new_node, self.end)
            self.position_map[0] = new_node
            return 0
        last_seat = -1
        max_distance = 0
        best_position = 0
        best_node = None
        current_node = self.start
        while current_node.next_node != self.end:
            current_node = current_node.next_node
            if last_seat == -1:
                max_distance = current_node.value
                best_node = current_node
            elif (current_node.value - last_seat) // 2 > max_distance:
                max_distance = (current_node.value - last_seat) // 2
                best_position = (current_node.value + last_seat) // 2
                best_node = current_node
            last_seat = current_node.value
        if self.total_seats - 1 - self.end.previous.value > max_distance:
            best_node = self.end
            best_position = self.total_seats - 1
        new_seat_node = NodeClass(best_position)
        self._connect(best_node.previous, new_seat_node)
        self._connect(new_seat_node, best_node)
        self.position_map[best_position] = new_seat_node
        return best_position
    def leave(self, seat_number: int):
        node_to_remove = self.position_map.pop(seat_number)
        self._connect(node_to_remove.previous, node_to_remove.next_node)
    def _connect(self, node_a: NodeClass, node_b: NodeClass):
        node_a.next_node = node_b
        node_b.previous = node_a
