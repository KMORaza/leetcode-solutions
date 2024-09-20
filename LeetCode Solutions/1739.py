class Solution:
    def minimumBoxes(self, x: int) -> int:
        box_count = 0
        current_step = 0
        level_box_count = 0
        while box_count < x:
            current_step += 1
            level_box_count += current_step
            box_count += level_box_count
        if box_count == x:
            return level_box_count
        box_count -= level_box_count
        level_box_count -= current_step
        current_step = 0
        while box_count < x:
            current_step += 1
            box_count += current_step
        return level_box_count + current_step
