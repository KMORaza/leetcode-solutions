class Solution:
    def minimumDeletions(self, elements):
        count = len(elements)
        min_value = float('inf')
        max_value = float('-inf')
        min_position = -1
        max_position = -1
        for index in range(count):
            if elements[index] < min_value:
                min_value = elements[index]
                min_position = index
            if elements[index] > max_value:
                max_value = elements[index]
                max_position = index
        if min_position < max_position:
            lower_index = min_position
            upper_index = max_position
        else:
            lower_index = max_position
            upper_index = min_position
        remove_both_sides = lower_index + 1 + (count - upper_index)
        remove_from_start = upper_index + 1
        remove_from_end = count - lower_index
        minimum_deletions = remove_both_sides
        if remove_from_start < minimum_deletions:
            minimum_deletions = remove_from_start
        if remove_from_end < minimum_deletions:
            minimum_deletions = remove_from_end
        return minimum_deletions
