from typing import List
from collections import defaultdict
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_food_count = defaultdict(lambda: defaultdict(int))
        food_items = set()
        for _, table, food in orders:
            table_food_count[table][food] += 1
            food_items.add(food)
        sorted_food_items = sorted(food_items)
        result = []
        header = ["Table"] + sorted_food_items
        result.append(header)
        for table in sorted(table_food_count.keys(), key=int):
            row = [table]
            for food in sorted_food_items:
                row.append(str(table_food_count[table][food]))
            result.append(row)
        return result
