from collections import deque, defaultdict
from typing import List
class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        new_group_index = m
        items_by_group = defaultdict(list)
        item_incoming_edges = [0] * n
        group_incoming_edges = [0] * (n + m)
        item_adjacency_list = defaultdict(list)
        group_adjacency_list = defaultdict(list)
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group_index
                new_group_index += 1
            items_by_group[group[i]].append(i)
        for i in range(n):
            for before_item_index in beforeItems[i]:
                if group[i] == group[before_item_index]:
                    item_incoming_edges[i] += 1
                    item_adjacency_list[before_item_index].append(i)
                else:
                    group_incoming_edges[group[i]] += 1
                    group_adjacency_list[group[before_item_index]].append(group[i])
        all_groups = list(range(n + m))
        sorted_groups = self.topologicalSort(group_incoming_edges, group_adjacency_list, all_groups)
        if not sorted_groups:
            return []
        sorted_items = []
        for gid in sorted_groups:
            group_items = items_by_group[gid]
            sorted_group_items = self.topologicalSort(item_incoming_edges, item_adjacency_list, group_items)
            if len(sorted_group_items) != len(group_items):
                return []
            sorted_items.extend(sorted_group_items)
        return sorted_items
    def topologicalSort(self, incoming_edges: List[int], adjacency_list: defaultdict, items: List[int]) -> List[int]:
        queue = deque()
        for i in items:
            if incoming_edges[i] == 0:
                queue.append(i)
        sorted_items = []
        while queue:
            current = queue.popleft()
            sorted_items.append(current)
            for next_item in adjacency_list[current]:
                incoming_edges[next_item] -= 1
                if incoming_edges[next_item] == 0:
                    queue.append(next_item)
        return sorted_items if len(sorted_items) == len(items) else []
