class ComponentTracker:
    def __init__(self, num_items):
        self.total_groups = num_items
        self.representative = list(range(num_items))
        self.group_size = [1] * num_items
    def merge_by_size(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        if self.group_size[root_a] < self.group_size[root_b]:
            self.group_size[root_b] += self.group_size[root_a]
            self.representative[root_a] = root_b
        else:
            self.group_size[root_a] += self.group_size[root_b]
            self.representative[root_b] = root_a
        self.total_groups -= 1
    def get_group_count(self):
        return self.total_groups
    def get_largest_group(self):
        return max(self.group_size)
    def find(self, item):
        if self.representative[item] != item:
            self.representative[item] = self.find(self.representative[item])
        return self.representative[item]
class Solution:
    def groupStrings(self, words):
        tracker = ComponentTracker(len(words))
        mask_map = {}
        altered_mask_map = {}
        for index, word in enumerate(words):
            bitmask = self.compute_bitmask(word)
            for position in range(26):
                if (bitmask >> position) & 1:
                    new_mask = bitmask ^ (1 << position)
                    if new_mask in mask_map:
                        tracker.merge_by_size(index, mask_map[new_mask])
                    if new_mask in altered_mask_map:
                        tracker.merge_by_size(index, altered_mask_map[new_mask])
                    else:
                        altered_mask_map[new_mask] = index
                else:
                    new_mask = bitmask | (1 << position)
                    if new_mask in mask_map:
                        tracker.merge_by_size(index, mask_map[new_mask])
            mask_map[bitmask] = index
        return [tracker.get_group_count(), tracker.get_largest_group()]
    def compute_bitmask(self, s):
        bitmask = 0
        for character in s:
            bitmask |= 1 << (ord(character) - ord('a'))
        return bitmask
