from dataclasses import dataclass
from typing import List, Optional
@dataclass
class Node:
    range_start: int
    range_end: int
    left_branch: Optional['Node'] = None
    right_branch: Optional['Node'] = None
    peak: int = 0
    total_count: int = 0
    def __init__(self, range_start: int, range_end: int, left_branch: Optional['Node'], right_branch: Optional['Node'], peak: int, total_count: int):
        self.range_start = range_start
        self.range_end = range_end
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.peak = peak
        self.total_count = total_count
class IntervalTree:
    def __init__(self, row_count: int, col_count: int):
        self.col_count = col_count
        self.root_node = self.construct(0, row_count - 1)
    def construct(self, low: int, high: int) -> Node:
        if low == high:
            return Node(low, high, None, None, self.col_count, self.col_count)
        mid = (low + high) // 2
        left_branch = self.construct(low, mid)
        right_branch = self.construct(mid + 1, high)
        return Node(
            low,
            high,
            left_branch,
            right_branch,
            max(left_branch.peak, right_branch.peak),
            left_branch.total_count + right_branch.total_count
        )
    def fetch_maximum_range(self, current_node: Node, required_count: int, max_row_index: int) -> List[int]:
        if current_node.range_start == current_node.range_end:
            if current_node.total_count < required_count or current_node.range_start > max_row_index:
                return []
            return [current_node.range_start, self.col_count - current_node.total_count]
        if current_node.left_branch.peak >= required_count:
            return self.fetch_maximum_range(current_node.left_branch, required_count, max_row_index)
        return self.fetch_maximum_range(current_node.right_branch, required_count, max_row_index)
    def compute_total_range(self, current_node: Node, start_index: int, end_index: int) -> int:
        if current_node.range_start == start_index and current_node.range_end == end_index:
            return current_node.total_count
        mid = (current_node.range_start + current_node.range_end) // 2
        if end_index <= mid:
            return self.compute_total_range(current_node.left_branch, start_index, end_index)
        if start_index > mid:
            return self.compute_total_range(current_node.right_branch, start_index, end_index)
        return self.compute_total_range(current_node.left_branch, start_index, mid) + self.compute_total_range(current_node.right_branch, mid + 1, end_index)
    def decrease(self, current_node: Node, target_row: int, decrement_value: int):
        if current_node is None:
            return
        if current_node.range_start == current_node.range_end and current_node.range_end == target_row:
            current_node.peak -= decrement_value
            current_node.total_count -= decrement_value
            return
        mid = (current_node.range_start + current_node.range_end) // 2
        if target_row <= mid:
            self.decrease(current_node.left_branch, target_row, decrement_value)
        else:
            self.decrease(current_node.right_branch, target_row, decrement_value)
        current_node.peak = max(current_node.left_branch.peak, current_node.right_branch.peak)
        current_node.total_count = current_node.left_branch.total_count + current_node.right_branch.total_count
class BookMyShow:
    def __init__(self, total_rows: int, total_columns: int):
        self.seat_structure = IntervalTree(total_rows, total_columns)
        self.remaining_seats = [total_columns] * total_rows
        self.first_empty_row = 0
    def gather(self, request_count: int, max_row_index: int) -> List[int]:
        result = self.seat_structure.fetch_maximum_range(self.seat_structure.root_node, request_count, max_row_index)
        if len(result) == 2:
            target_row = result[0]
            self.seat_structure.decrease(self.seat_structure.root_node, target_row, request_count)
            self.remaining_seats[target_row] -= request_count
        return result
    def scatter(self, request_count: int, max_row_index: int) -> bool:
        if self.seat_structure.compute_total_range(self.seat_structure.root_node, 0, max_row_index) < request_count:
            return False
        while request_count > 0:
            if self.remaining_seats[self.first_empty_row] >= request_count:
                self.seat_structure.decrease(self.seat_structure.root_node, self.first_empty_row, request_count)
                self.remaining_seats[self.first_empty_row] -= request_count
                request_count = 0
            else:
                self.seat_structure.decrease(self.seat_structure.root_node, self.first_empty_row, self.remaining_seats[self.first_empty_row])
                request_count -= self.remaining_seats[self.first_empty_row]
                self.remaining_seats[self.first_empty_row] = 0
                self.first_empty_row += 1
        return True
