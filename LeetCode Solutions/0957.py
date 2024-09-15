from typing import List
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_state(cells: List[int]) -> List[int]:
            new_cells = [0] * 8
            for i in range(1, 7):
                new_cells[i] = 1 if cells[i-1] == cells[i+1] else 0
            return new_cells
        seen = {}
        state = tuple(cells)
        for day in range(n):
            if state in seen:
                cycle_length = day - seen[state]
                remaining_days = (n - day) % cycle_length
                for _ in range(remaining_days):
                    state = tuple(next_state(list(state)))
                return list(state)
            seen[state] = day
            state = tuple(next_state(list(state)))
        return list(state)
