from collections import deque
class Solution:
    def maxCandies(self, box_status, box_candies, box_keys, nested_boxes, start_boxes):
        total_sweets = 0
        queue = deque()
        box_reached_status = [False] * len(box_status)
        def add_accessible_boxes(boxes, box_status, queue, box_reached_status):
            for box in boxes:
                if box_status[box] == 1:
                    queue.append(box)
                else:
                    box_reached_status[box] = True
        add_accessible_boxes(start_boxes, box_status, queue, box_reached_status)
        while queue:
            current_box = queue.popleft()
            total_sweets += box_candies[current_box]
            for key in box_keys[current_box]:
                if box_status[key] == 0 and box_reached_status[key]:
                    queue.append(key)
                box_status[key] = 1
            add_accessible_boxes(nested_boxes[current_box], box_status, queue, box_reached_status)
        return total_sweets