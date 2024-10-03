class Solution:
    def maximumTop(self, items: list[int], operations: int) -> int:
        if operations == 0:
            return items[0]
        total_items = len(items)
        if total_items == 1:
            if operations % 2 == 1:
                return -1
            return items[0]
        best_value = -1
        for pos in range(min(operations - 1, total_items)):
            best_value = max(best_value, items[pos])
        if operations < total_items:
            best_value = max(best_value, items[operations])
        return best_value